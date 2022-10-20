#pragma once

#include "App/Extensions/ModuleBase.hpp"

namespace App
{
struct FactoryIndexUnit : ConfigurableUnit
{
    using ConfigurableUnit::ConfigurableUnit;

    bool IsDefined() override;
    void LoadYAML(const YAML::Node& aNode) override;

    Core::Vector<std::string> factories;
};
}
