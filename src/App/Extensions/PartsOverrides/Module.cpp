#include "Module.hpp"
#include "Red/Entity.hpp"

namespace
{
constexpr auto ModuleName = "PartsOverrides";
constexpr auto EnableDebugOutput = false;
}

std::string_view App::PartsOverridesModule::GetName()
{
    return ModuleName;
}

bool App::PartsOverridesModule::Load()
{
    if (!HookBefore<Raw::GarmentAssembler::AddItem>(&OnAddGarmentItem))
        throw std::runtime_error("Failed to hook [GarmentAssembler::AddItem].");

    if (!HookBefore<Raw::GarmentAssembler::OverrideItem>(&OnOverrideGarmentItem))
        throw std::runtime_error("Failed to hook [GarmentAssembler::OverrideItem].");

    if (!HookBefore<Raw::GarmentAssembler::RemoveItem>(&OnRemoveGarmentItem))
        throw std::runtime_error("Failed to hook [GarmentAssembler::RemoveItem].");

    if (!HookBefore<Raw::GarmentAssembler::OnGameDetach>(&OnGameDetach))
        throw std::runtime_error("Failed to hook [GarmentAssembler::OnGameDetach].");

    if (!HookBefore<Raw::AppearanceChanger::ComputePlayerGarment>(&OnComputeGarment))
        throw std::runtime_error("Failed to hook [AppearanceChanger::ComputePlayerGarment].");

    if (!HookBefore<Raw::Entity::ReassembleAppearance>(&OnReassembleAppearance))
        throw std::runtime_error("Failed to hook [Entity::ReassembleAppearance].");

    s_states = Core::MakeUnique<OverrideStateManager>();

    return true;
}

bool App::PartsOverridesModule::Unload()
{
    Unhook<Raw::GarmentAssembler::AddItem>();
    Unhook<Raw::GarmentAssembler::OverrideItem>();
    Unhook<Raw::GarmentAssembler::RemoveItem>();
    Unhook<Raw::GarmentAssembler::OnGameDetach>();
    Unhook<Raw::AppearanceChanger::ComputePlayerGarment>();
    Unhook<Raw::Entity::ReassembleAppearance>();

    s_states.reset();

    return true;
}

void App::PartsOverridesModule::OnAddGarmentItem(uintptr_t, Red::WeakHandle<Red::ent::Entity>& aEntityWeak,
                                                 Red::GarmentItemAddRequest& aRequest)
{
    if (auto entity = aEntityWeak.Lock())
    {
        std::lock_guard _(s_lock);
        if (auto& entityState = s_states->GetEntityState(entity))
        {
            RegisterOverrides(entityState, aRequest.hash, aRequest.apperance);
        }
    }
}

void App::PartsOverridesModule::OnOverrideGarmentItem(uintptr_t, Red::WeakHandle<Red::ent::Entity>& aEntityWeak,
                                                      Red::GarmentItemOverrideRequest& aRequest)
{
    if (auto entity = aEntityWeak.Lock())
    {
        std::lock_guard _(s_lock);
        if (auto& entityState = s_states->GetEntityState(entity))
        {
            RegisterOverrides(entityState, aRequest.hash, aRequest.apperance);
        }
    }
}

void App::PartsOverridesModule::OnRemoveGarmentItem(uintptr_t, Red::WeakHandle<Red::ent::Entity>& aEntityWeak,
                                                    Red::GarmentItemRemoveRequest& aRequest)
{
    if (auto entity = aEntityWeak.Lock())
    {
        std::lock_guard _(s_lock);
        if (auto& entityState = s_states->GetEntityState(entity))
        {
            UnregisterOverrides(entityState, aRequest.hash);
        }
    }
}

void App::PartsOverridesModule::OnComputeGarment(Red::Handle<Red::ent::Entity>& aEntity, uintptr_t,
                                                 Red::SharedPtr<Red::GarmentComputeData>& aData, uintptr_t,
                                                 uintptr_t, uintptr_t, bool)
{
    if (auto& entityState = s_states->FindEntityState(aEntity))
    {
        std::lock_guard _(s_lock);
        ApplyOverrides(entityState, aData->components);
    }
}

void App::PartsOverridesModule::OnReassembleAppearance(Red::ent::Entity* aEntity, uintptr_t, uintptr_t, uintptr_t,
                                                       uintptr_t, uintptr_t)
{
    if (auto& entityState = s_states->FindEntityState(aEntity))
    {
        std::lock_guard _(s_lock);
        ApplyOverrides(entityState, true);
    }
}

void App::PartsOverridesModule::OnGameDetach(uintptr_t)
{
    std::lock_guard _(s_lock);
    s_states->Reset();
}

void App::PartsOverridesModule::RegisterOverrides(Core::SharedPtr<EntityState>& aEntityState, uint64_t aHash,
                                                  Red::Handle<Red::AppearanceDefinition>& aApperance)
{
    for (const auto& partOverrides : aApperance->partsOverrides)
    {
        if (!partOverrides.partResource.path)
        {
            for (const auto& componentOverride : partOverrides.componentsOverrides)
            {
                aEntityState->AddOverride(aHash, componentOverride.componentName, componentOverride.chunkMask);
            }
        }
    }

    for (const auto& visualTag : aApperance->visualTags.tags)
    {
        aEntityState->AddOverrideTag(aHash, visualTag);
    }
}

void App::PartsOverridesModule::UnregisterOverrides(Core::SharedPtr<EntityState>& aEntityState, uint64_t aHash)
{
    aEntityState->RemoveOverrides(aHash);
}

void App::PartsOverridesModule::ApplyOverrides(Core::SharedPtr<EntityState>& aEntityState,
                                               Red::DynArray<Red::Handle<Red::ent::IComponent>>& aComponents,
                                               bool aVerbose)
{
    auto index = 0;

    for (auto& component : aComponents)
    {
        aEntityState->ApplyOverrides(component);

        if (EnableDebugOutput && aVerbose && component->isEnabled)
        {
            LogDebug("|{}| [entity={} index={} component={} type={}].",
                     ModuleName,
                     aEntityState->GetName(),
                     index++,
                     component->name.ToString(),
                     component->GetType()->GetName().ToString());
        }
    }
}

void App::PartsOverridesModule::ApplyOverrides(Core::SharedPtr<EntityState>& aEntityState, bool aVerbose)
{
    ApplyOverrides(aEntityState, Raw::Entity::GetComponents(aEntityState->GetEntity()), aVerbose);
}
