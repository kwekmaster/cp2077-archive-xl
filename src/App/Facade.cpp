#include "Facade.hpp"
#include "App/Project.hpp"
#include "App/Extensions/ExtensionService.hpp"
#include "Core/Facades/Container.hpp"

void App::Facade::Reload()
{
    Core::Resolve<ExtensionService>()->Configure();
}

bool App::Facade::Require(Red::CString& aVersion)
{
    const auto requirement = semver::from_string_noexcept(aVersion.c_str());
    return requirement.has_value() ? Project::Version >= requirement.value() : false;
}

Red::CString App::Facade::GetVersion()
{
    return Project::Version.to_string().c_str();
}

void App::Facade::OnRegister(Descriptor* aType)
{
    aType->SetName(Project::Name);
    aType->SetFlags({ .isAbstract = true });
}

void App::Facade::OnDescribe(Descriptor* aType)
{
    aType->AddFunction<&Reload>("Reload");
    aType->AddFunction<&Require>("Require");
    aType->AddFunction<&GetVersion>("Version");
}
