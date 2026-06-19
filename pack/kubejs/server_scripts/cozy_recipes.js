// =============================================================================
// Cozy Farming SMP — Rezept-Anpassungen (KubeJS, server_scripts)
// IDs gegen die echten Mod-Jars verifiziert. Nach Änderungen: /reload + EMI prüfen.
// Materialien-Dedup (#14) übernimmt der Mod "Almost Unified" automatisch — daher hier nicht.
// =============================================================================

ServerEvents.recipes(event => {

  // ── #1/#2  Münz-Wirtschaft vereinheitlichen ────────────────────────────────
  // Magic-Coins-Tiers beidseitig: 9 Silber = 1 Gold, 9 Gold = 1 Kristall.
  event.shapeless('magic_coins:gold_coin',      ['9x magic_coins:silver_coin'])
  event.shapeless('9x magic_coins:silver_coin', ['magic_coins:gold_coin'])
  event.shapeless('magic_coins:crystal_coin',   ['9x magic_coins:gold_coin'])
  event.shapeless('9x magic_coins:gold_coin',   ['magic_coins:crystal_coin'])
  // Brücke Magic Coins ↔ Create: Numismatics (Rate frei wählbar):
  event.shapeless('magic_coins:gold_coin', ['8x numismatics:cog'])
  event.shapeless('8x numismatics:cog',    ['magic_coins:gold_coin'])

  // ── #3  Create-Einstieg: Andesite Alloy von Hand (Bootstrap) ───────────────
  event.shapeless('create:andesite_alloy', ['minecraft:andesite', 'minecraft:iron_nugget'])

  // ── #5  Gleise günstiger -> fördert das Zug-Netz (zusätzliches Rezept) ─────
  event.shaped('8x create:track', ['NAN', 'W W', 'NAN'], {
    N: 'minecraft:iron_nugget', A: 'create:andesite_alloy', W: '#minecraft:wooden_slabs'
  })

  // ── #6  Super Glue günstiger (Kontraptionen sind Kernspaß) ─────────────────
  event.remove({ output: 'create:super_glue' })
  event.shapeless('4x create:super_glue', ['minecraft:slime_ball', 'minecraft:paper'])

  // ── #8  Rich Soil leichter -> frühes Farmen belohnen ───────────────────────
  event.shapeless('2x farmersdelight:rich_soil',
    ['minecraft:dirt', 'minecraft:dirt', 'farmersdelight:organic_compost'])

  // ── #16  MineColonies Bau-Werkzeug nie als Sackgasse (einfach craftbar) ────
  event.shaped('minecolonies:sceptergold', ['G', 'S'], {
    G: 'minecraft:gold_ingot', S: 'minecraft:stick'
  })

  // ───────────────────────────────────────────────────────────────────────────
  // VORLAGEN — IDs aus EMI eintragen, dann // entfernen. (Rest der Top-20)
  // ───────────────────────────────────────────────────────────────────────────

  // #4  Erz-Verdopplung konsistent (KubeJS Create). Pro modded Erz wiederholen:
  // event.recipes.create.crushing(['2x modid:raw_xxx', Item.of('modid:raw_xxx').withChance(0.25)], 'modid:xxx_ore')

  // #7  Messing absichern (Kupfer+Zink -> Messing, beheizt):
  // event.recipes.create.mixing('create:brass_ingot', ['#c:ingots/copper', '#c:ingots/zinc']).heated()

  // #9  Kochtopf günstiger (Alternativ-Rezept mit weniger Eisen):
  // event.shaped('farmersdelight:cooking_pot', ['B B','IWI',' I '], {B:'minecraft:brick', I:'minecraft:iron_ingot', W:'minecraft:water_bucket'})

  // #10/#11  Bulk-Kochen / Kompost-Loop: überschüssige Crops -> Kompost/Bonemeal
  // event.shapeless('4x minecraft:bone_meal', ['4x #c:crops/wheat'])  // Tag in EMI prüfen

  // #12  Doppelte Messer der *-Delight-Addons auf eines reduzieren:
  // event.remove({ id: 'someaddon:knife_recipe_id' })

  // #13  Crop-Sorten vereinheitlichen (Tags) — ergänzt Almost Unified:
  // event.replaceInput({}, '#c:vegetables/tomato', 'farmersdelight:tomato')

  // #15  Every-Compat-Flut in EMI eindämmen (einzelne Rezepte entfernen):
  // event.remove({ mod: 'everycomp', output: 'everycomp:unwanted_block' })

  // #17  MineColonies-Baustoffe per Create zugänglich (Cutting/Stonecutting):
  // event.recipes.create.cutting('domum_ornamentum:xxx', 'minecraft:stone')

  // #18  Aeronautics-Propeller an Create-Wellen koppeln:
  // event.shaped('aeronautics:wooden_propeller', [' P ','PSP',' P '], {P:'#minecraft:planks', S:'create:shaft'})

  // #19  Levitite-Kette leicht verteuern (Endgame-Gate) — IDs aus EMI:
  // event.remove({ output: 'aeronautics:levitite' }); event.recipes.create.mixing('aeronautics:levitite', [...])

  // #20  Billige Wege zu Nether-Star/Diamant/Netherite schließen (Quest-Sinn):
  // event.remove({ output: 'minecraft:nether_star' })   // entfernt NUR modded Crafts (Vanilla = Boss-Drop)
})
