from cp77ida import Item, Group, Output, scan
from pathlib import Path


# Defines patterns and output files
def patterns():
    return [
        Output(filename="src/Red/Addresses.hpp", namespace="Red::Addresses", groups=[
            Group(functions=[
                Item(name="Main",
                     pattern="40 53 48 81 EC ? ? ? ? FF 15 ? ? ? ? E8 ? ? ? ? E8 ? ? ? ?"),
                Item(name="IsMainThread",
                     pattern="83 3D  ?  ? ? ? 00 74 17 65 48 8B 04 25 30 00 00 00 8B 48 48 39 0D ? ? ? ? 74 03 32 C0 C3"),
            ]),
            Group(name="AppearanceChanger", functions=[
                Item(name="ComputePlayerGarment",
                     pattern="48 89 5C 24 08 48 89 74 24 10 48 89 7C 24 18 4C 89 64 24 20 55 41 56 41 57 48 8D 6C 24 C0"),
            ]),
            Group(name="AppearanceChangeRequest", functions=[
                Item(name="LoadEntityTemplate",
                     pattern="48 89 5C 24 18 48 89 74 24 20 55 57 41 56 48 8D 6C 24 B9 48 81 EC C0 00 00 00 45 32 F6 48 8B F9"),
            ]),
            Group(name="AppearanceChangeSystem", functions=[
                Item(name="ChangeAppearance",
                     pattern="4C 8B DC 49 89 53 10 49 89 4B 08 55 53 56 41 54 41 57 49 8D AB 58 FE FF FF 48 81 EC 80 02 00 00"),
            ]),
            Group(name="AppearanceNameVisualTagsPreset", functions=[
                Item(name="GetVisualTags",
                     pattern="48 89 74 24 18 48 89 54 24 10 57 48 83 EC 40 49 8B F8 48 8D 54 24 20 4C 8D 44 24 58 48 83 C1 40 49 8B F1"),
            ]),
            Group(name="AppearanceResource", functions=[
                Item(name="FindAppearanceDefinition",
                     pattern="48 89 5C 24 08 48 89 6C 24 10 48 89 74 24 18 57 41 56 41 57 48 83 EC 20 48 8B F1 45 8B F9 48 81 C1 F0 00 00 00 49 8B D8 4C 8B F2"),
            ]),
            Group(name="AttachmentSlots", functions=[
                Item(name="InitializeSlots",
                     pattern="48 8B C4 55 57 48 8D 68 B8 48 81 EC 38 01 00 00 83 7A 0C 00 48 8B FA"),
                Item(name="IsSlotEmpty",
                     pattern="48 89 5C 24 08 48 89 74 24 10 57 48 83 EC 20 48 8B F1 48 8B DA 48 81 C1 00 01 00 00",
                     expected=4,
                     index=1),
                Item(name="IsSlotSpawning",
                     pattern="48 89 5C 24 08 48 89 74 24 10 57 48 83 EC 20 48 8B F1 48 8B DA 48 81 C1 00 01 00 00",
                     expected=4,
                     index=2),
            ]),
            Group(name="CBaseEngine", functions=[
                Item(name="LoadGatheredResources",
                     pattern="40 53 48 83 EC 70 48 8B 01 FF 90 A0 00 00 00 33 DB 84 C0 8B CB 0F 95 C1 E8"),
            ]),
            Group(name="CharacterCustomizationFeetController", functions=[
                Item(name="CheckState",
                     pattern="48 8B C4 41 54 48 83 EC 70 48 89 58 20 48 89 78 E0 48 8B F9 4C 89 68 D8 4C 89 70 D0 4D 8B F0"),
                Item(name="GetOwner",
                     pattern="48 89 5C 24 10 48 89 6C 24 18 48 89 74 24 20 57 48 83 EC 40 48 8B 79 50 33 ED 89 6C 24 50 48 8B DA 48 85 FF 74",
                     expected=2,
                     index=1),
            ]),
            Group(name="CharacterCustomizationHelper", functions=[
                Item(name="GetHairColor",
                     pattern="40 55 41 56 41 57 48 8B EC 48 83 EC 50 4C 8B F9 48 8B 0A 48 8D 55 D8 48 8B 01 FF 90 E8 01 00 00"),
            ]),
            Group(name="CharacterCustomizationSystem", functions=[
                Item(name="Initialize",
                     pattern="48 8B C4 44 88 40 18 48 89 50 10 55 56 48 8D 68 A1 48 81 EC E8 00 00 00 48 89 58 20 4C 89 68 D8"),
                Item(name="Uninitialize",
                     pattern="40 53 56 57 48 83 EC 50 48 8B F1 48 83 C1 78 E8 ? ? ? ? 48 8B 86 F8 00 00 00 33 FF 0F 57 C0"),
                Item(name="EnsureState",
                     pattern="48 8B C4 55 41 57 48 8D A8 38 FF FF FF 48 81 EC B8 01 00 00 48 89 58 08 48 89 78 20 48 8B F9"),
                Item(name="InitializeAppOption",
                     pattern="4C 8B DC 48 81 EC 98 00 00 00 49 89 5B 08 49 8B D9 49 89 73 F8 48 8B F1 49 8B 08 4D 89 63 E8"),
                Item(name="InitializeMorphOption",
                     pattern="48 8B C4 55 57 48 8D 68 A1 48 81 EC D8 00 00 00 48 89 58 08 49 8B D8 4C 89 60 20 4D 8B E1"),
                Item(name="InitializeSwitcherOption",
                     pattern="48 8B C4 44 89 48 20 4C 89 40 18 89 50 10 55 41 57 48 8D 68 B1 48 81 EC E8 00 00 00 48 89 70 E8"),
            ]),
            Group(name="CMesh", functions=[
                Item(name="GetAppearance",
                     pattern="40 53 48 83 EC 20 4C 8B 81 E0 01 00 00 48 8B D9 8B 81 EC 01 00 00 48 C1 E0 04 49 03 C0 4C 3B C0"),
            ]),
            Group(name="Entity", functions=[
                Item(name="GetComponents",
                     pattern="48 83 C1 70 E9",
                     expected=7,
                     index=1),
                Item(name="ReassembleAppearance",
                     pattern="40 55 53 56 57 41 54 41 55 41 56 41 57 48 8D 6C 24 88 48 81 EC 78 01 00 00 4C 8B EA 49 8B D9"),
            ]),
            Group(name="EntityTemplate", functions=[
                Item(name="FindAppearance",
                     pattern="40 53 48 83 EC 20 48 8B  D9 48 85 D2 74 ? 48 3B 15 ? ? ? ? 75 ? 48  8B 51 60 48 3B 15 ? ? ? ? 48 89 7C 24 30 75"),
            ]),
            Group(name="FactoryIndex", functions=[
                Item(name="LoadFactoryAsync",
                     pattern="48 89 5C 24 18 55 56 57 41 56 41 57 48 8D 6C 24 C9 48 81 EC A0 00 00 00 45 33 FF 48 89 55 DF 4D 8B F0 44 89 7D FB 48 8B D9 4C 89 7D E7"),
                Item(name="ResolveResource",
                     pattern="40 53 48 83 EC 10 45 33 C9 48 8B DA 4C 8B D1 44 39 49 70"),
            ]),
            Group(name="GameApplication", functions=[
                Item(name="InitResourceDepot",
                     pattern="48 89 74 24 18 55 48 8D 6C 24 A9 48 81 EC C0 00 00 00"),
            ]),
            Group(name="GarmentAssembler", functions=[
                Item(name="AddItem",
                     pattern="48 89 5C 24 08 57 48 83 EC 60 49 8B F8 4C 8B C2 48 8D 54 24 40 E8 ? ? ? ? 48 8B 07",
                     expected=2,
                     index=0),
                Item(name="AddCustomItem",
                     pattern="48 89 5C 24 08 57 48 83 EC 60 49 8B F8 4C 8B C2 48 8D 54 24 40 E8 ? ? ? ? 48 8B 07",
                     expected=2,
                     index=1),
                Item(name="ChangeItem",
                     pattern="48 89 5C 24 08 48 89 6C 24 10 48 89 74 24 18 57 48 83 EC 50 49 8B F8 4C 8B C2 48 8D 54 24 30 E8",
                     expected=2,
                     index=0),
                Item(name="ChangeCustomItem",
                     pattern="48 89 5C 24 08 48 89 6C 24 10 48 89 74 24 18 57 48 83 EC 50 49 8B F8 4C 8B C2 48 8D 54 24 30 E8",
                     expected=2,
                     index=1),
                Item(name="RemoveItem",
                     pattern="48 89 5C 24 08 57 48 83 EC 40 49 8B F8 4C 8B C2 48 8D 54 24 20 E8 ? ? ? ? 44 8B 47"),
                Item(name="OnGameDetach",
                     pattern="40 53 48 83 EC 20 8B 51 14 48 8B D9 48 8B 49 08 E8 ? ? ? ? C7 43 14 00 00 00 00",
                     expected=2,
                     index=1),
            ]),
            Group(name="InkSpawner", functions=[
                Item(name="FinishAsyncSpawn",
                     pattern="48 89 5C 24 10 57 48 83 EC 30 48 8B 42 08 48 8B DA 4C 8B 0A 48 8B F9 4C 8B 41 18 4C 89 4C 24 20"),
            ]),
            Group(name="InkWidgetLibrary", functions=[
                Item(name="AsyncSpawnFromExternal",
                     pattern="48 89 5C 24 08 57 48 83 EC 40 48 8B FA 49 8B D9 48 8D 54 24 28 E8 ? ? ? ? 48 8B 4C 24 28 48 85 C9 74 ? 48 8B D3 E8",
                     expected=2,
                     index=0),
                Item(name="AsyncSpawnFromLocal",
                     pattern="48 89 5C 24 08 57 48 83 EC 20 48 8B FA 41 0F B6 D9 49 8B D0 E8 ? ? ? ? 48 85 C0 74"),
                Item(name="SpawnFromExternal",
                     pattern="48 89 5C 24 08 57 48 83 EC 40 48 8B FA 49 8B D9 48 8D 54 24 28 E8 ? ? ? ? 48 8B 4C 24 28 48 85 C9 74 ? 48 8B D3 E8",
                     expected=2,
                     index=1),
                Item(name="SpawnFromLocal",
                     pattern="40 53 48 83 EC 20 48 8B DA 49 8B D0 E8 ? ? ? ? 48 85 C0 74 ? 48 8B  D3 48 8B C8 E8",
                     expected=2,
                     index=1),
            ]),
            Group(name="JobHandle", functions=[
                Item(name="Wait",
                     pattern="40 53 48 83 EC 30 48 8B D9 33 D2 48 8B 0D BE BB 07 02 E8"),
            ]),
            Group(name="JournalManager", functions=[
                Item(name="LoadJournal",
                     pattern="48 89 5C 24 20 55 56 57 41 54 41 55 41 56 41 57 48 8D 6C 24 D9 48 81 EC D0 00 00 00 4C 8B E2"),
                Item(name="GetEntryHash",
                     pattern="48 89 5C 24 10 48 89 6C 24 18 48 89 74 24 20 57 48 83 EC 20 33 F6 48 8B EA 8B DE 48 8B F9 66 90"),
                Item(name="GetEntryByHash",
                     pattern="48 89 5C 24 08 48 89 6C 24 10 48 89 74 24 18 48 89 7C 24 20 41 56 48 83 EC 20 33 F6 41 8B E8"),
                Item(name="GetTrackedQuest",
                     pattern="48 8B 81 10 01 00 00 48 89 02 48 8B 81 18 01 00 00 48 89 42 08 48 85 C0 74 ? F0 FF 00 48 8B C2"),
                Item(name="GetTrackedPointOfInterest",
                     pattern="48 8B 81 20 01 00 00 48 89 02 48 8B 81 28 01 00 00 48 89 42 08 48 85 C0 74 ? F0 FF 00 48 8B C2"),
                Item(name="TrackQuest",
                     pattern="48 89 54 24 10 55 53 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 18 FF FF FF 48 81 EC E8 01 00 00 48 8B 1A 45 32 ED 4C 8B F2 48 8B F1"),
                Item(name="TrackPointOfInterest",
                     pattern="48 81 C1 20 01 00 00 E9",
                     expected=8),
            ]),
            Group(name="JournalRootFolderEntry", functions=[
                Item(name="Initialize",
                     pattern="48 89 5C 24 08 48 89 74 24 10 57 48 83 EC 20 4D 8B C1 49 8B F1 48 8B DA 48 8B F9 E8"),
            ]),
            Group(name="JournalTree", functions=[
                Item(name="ProcessJournalIndex",
                     pattern="48 89 4C 24 08 55 41 56 48 81 EC B8 00 00 00 4C 8B F1 48 8B EA 48 8B 49 08 E8"),
            ]),
            Group(name="Localization", functions=[
                Item(name="LoadOnScreens",
                     pattern="40 55 53 57 48 8B EC 48 81 EC 80 00 00 00 0F 57 C0 48 8B D9 F3 0F 7F 45 A0 48 85 D2 75 17 33 FF 48 8B C1 48 89 39 48 89 79 08 48 81 C4 80 00 00",
                     expected=2),
            ]),
            Group(name="MeshAppearance", functions=[
                Item(name="LoadMaterialSetupAsync",
                     pattern="40 55 53 56 57 41 55 41 57 48 8D AC 24 78 FF FF FF 48 81 EC 88 01 00 00 45 0F B6 E8 48 8B F2 4C"),
            ]),
            Group(name="ResourceLoader", functions=[
                Item(name="OnUpdate",
                     pattern="48 8B 49 48 48 85 C9 0F 85",
                     expected=9,
                     index=2),
            ]),
            Group(name="StreamingWorld", functions=[
                Item(name="OnLoad",
                     pattern="48 89 5C 24 08 57 48 83 EC 40 48 8B FA 48 8B D9 E8 ? ? ? ? 0F 57 C0 48 8D 93 D8 01 00 00"),
            ]),
            Group(name="TagList", functions=[
                Item(name="MergeWith",
                     pattern="48 89 5C 24 08 48 89 74 24 10 57 48 83 EC 20 48 8B 1A 48 8B F1 8B 42 0C 48 8D 3C C3 48 3B DF 74"),
            ]),
            Group(name="TPPRepresentationComponent", functions=[
                Item(name="OnAttach",
                     pattern="48 89 54 24 10 55 53 56 57 41 56 41 57 48 8D AC 24 E8 FE FF FF 48 81 EC 18 02 00 00 45 33 F6"),
            ]),
            Group(name="TransactionSystem", functions=[
                Item(name="IsSlotSpawning",
                     pattern="40 53 48 83 EC 30 49 8B D8 4C 8B C2 48 8D 54 24 20 E8 ? ? ? ? 48 8B 4C 24 20 48 85 C9 75 04 32 DB EB ? 48 8B D3 E8 ? ? ? ? 0F B6 D8",
                     expected=3,
                     index=1),
            ]),
        ]),
    ]


# Defines base output dir
def output_dir():
    cwd = Path(__file__).resolve().parent
    return cwd.parent.parent  # 2 levels up


scan(patterns(), output_dir(), __file__)
