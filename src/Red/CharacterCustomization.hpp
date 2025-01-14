#pragma once

#include "Core/Raw.hpp"
#include "Red/Addresses.hpp"

namespace Red
{
enum class CharacterFeetState : uint32_t
{
    Undefined = 0,
    Flat = 1,
    Lifted = 2,
};
}

namespace Raw::CharacterCustomizationFeetController
{
constexpr auto GetOwner = Core::RawFunc<
    /* addr = */ Red::Addresses::CharacterCustomizationFeetController_GetOwner,
    /* type = */ void (*)(Red::game::ui::CharacterCustomizationFeetController* aComponent,
                          Red::Handle<Red::IScriptable>& aOwner)>();

constexpr auto CheckState = Core::RawFunc<
    /* addr = */ Red::Addresses::CharacterCustomizationFeetController_CheckState,
    /* type = */ void (*)(Red::game::ui::CharacterCustomizationFeetController* aComponent,
                          Red::CharacterFeetState& aLiftedState,
                          Red::CharacterFeetState& aFlatState)>();
}

namespace Raw::CharacterCustomizationSystem
{
constexpr auto Initialize = Core::RawFunc<
    /* addr = */ Red::Addresses::CharacterCustomizationSystem_Initialize,
    /* type = */ void (*)(Red::game::ui::ICharacterCustomizationSystem& aSystem,
                          Red::Handle<Red::game::Puppet>& aPuppet, bool aIsMale, uintptr_t a4)>();

constexpr auto Uninitialize = Core::RawFunc<
    /* addr = */ Red::Addresses::CharacterCustomizationSystem_Uninitialize,
    /* type = */ void (*)(Red::game::ui::ICharacterCustomizationSystem& aSystem)>();

constexpr auto EnsureState = Core::RawFunc<
    /* addr = */ Red::Addresses::CharacterCustomizationSystem_EnsureState,
    /* type = */ void (*)(Red::game::ui::ICharacterCustomizationSystem& aSystem,
                          Red::Handle<Red::game::ui::CharacterCustomizationState>& aState)>();

constexpr auto InitializeAppOption = Core::RawFunc<
    /* addr = */ Red::Addresses::CharacterCustomizationSystem_InitializeAppOption,
    /* type = */ void (*)(Red::game::ui::ICharacterCustomizationSystem& aSystem,
                          Red::game::ui::CharacterCustomizationPart aPartType,
                          Red::Handle<Red::game::ui::CharacterCustomizationOption>& aOption,
                          Red::SortedUniqueArray<Red::CName>& aStateOptions,
                          Red::Map<Red::CName, Red::Handle<Red::game::ui::CharacterCustomizationOption>>& aUiSlots)>();

constexpr auto InitializeMorphOption = Core::RawFunc<
    /* addr = */ Red::Addresses::CharacterCustomizationSystem_InitializeMorphOption,
    /* type = */ void (*)(Red::game::ui::ICharacterCustomizationSystem& aSystem,
                          Red::Handle<Red::game::ui::CharacterCustomizationOption>& aOption,
                          Red::SortedUniqueArray<Red::CName>& aStateOptions,
                          Red::Map<Red::CName, Red::Handle<Red::game::ui::CharacterCustomizationOption>>& aUiSlots)>();

constexpr auto InitializeSwitcherOption = Core::RawFunc<
    /* addr = */ Red::Addresses::CharacterCustomizationSystem_InitializeSwitcherOption,
    /* type = */ bool (*)(Red::game::ui::ICharacterCustomizationSystem& aSystem,
                          Red::game::ui::CharacterCustomizationPart aPartType,
                          Red::Handle<Red::game::ui::CharacterCustomizationOption>& aOption,
                          int32_t aCurrentIndex,
                          uint64_t a5,
                          Red::Map<Red::CName, Red::Handle<Red::game::ui::CharacterCustomizationOption>>& aUiSlots)>();
}

namespace Raw::CharacterCustomizationHelper
{
constexpr auto GetHairColor = Core::RawFunc<
    /* addr = */ Red::Addresses::CharacterCustomizationHelper_GetHairColor,
    /* type = */ void (*)(Red::CName& aOut, Red::WeakHandle<Red::ISerializable>& aSystem, bool aIsMale)>();
}
