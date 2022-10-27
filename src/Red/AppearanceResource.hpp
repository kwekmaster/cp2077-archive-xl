#pragma once

#include "Core/Raw.hpp"
#include "Red/Addresses.hpp"

namespace Red
{
using AppearanceResource = appearance::AppearanceResource;
using AppearanceDefinition = appearance::AppearanceDefinition;
}

namespace Raw::AppearanceResource
{
constexpr auto FindAppearanceDefinition = Core::RawFunc<
    /* addr = */ Red::Addresses::AppearanceResource_FindAppearanceDefinition,
    /* type = */ uintptr_t (*)(Red::AppearanceResource* aResource, Red::Handle<Red::AppearanceDefinition>* aDefinition,
                               Red::CName aName, uint32_t, uint8_t)>();
}