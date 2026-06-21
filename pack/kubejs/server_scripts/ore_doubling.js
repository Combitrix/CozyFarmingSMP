// Cozy Farming SMP — Ore Doubling via Create Compacting
// Nachbau von "Create: Simple Ore Doubling" (ohne dessen Slag-Item).
// Mechanik: Mechanical Press auf einem Basin ("Compacting").
//   2x-Variante: rohes Erz + 50mb Lava        -> 2x Crushed Raw   (kein Heat)
//   3x-Variante: rohes Erz (Blaze Burner heat) -> 3x Crushed Raw   (heated)
// Nur Creates native Metalle (crushed_raw_* garantiert vorhanden). Rein additiv,
// kein Konflikt mit Creates normalen Crushing-Rezepten (anderer Recipe-Typ).

ServerEvents.recipes(event => {
  // [rohes Erz, Create-Crushed-Item]
  const metals = [
    ['minecraft:raw_iron',   'create:crushed_raw_iron'],
    ['minecraft:raw_gold',   'create:crushed_raw_gold'],
    ['minecraft:raw_copper', 'create:crushed_raw_copper'],
    ['create:raw_zinc',      'create:crushed_raw_zinc'],
  ]

  metals.forEach(([raw, crushed], i) => {
    // 2x — verbraucht 50mb Lava, kein Heat nötig
    event.custom({
      type: 'create:compacting',
      ingredients: [
        { item: raw },
        { type: 'fluid_stack', amount: 50, fluid: 'minecraft:lava' },
      ],
      results: [{ count: 2, id: crushed }],
    }).id(`kubejs:ore_doubling/2x_${i}`)

    // 3x — braucht einen befeuerten Blaze Burner (heated)
    event.custom({
      type: 'create:compacting',
      heat_requirement: 'heated',
      ingredients: [{ item: raw }],
      results: [{ count: 3, id: crushed }],
    }).id(`kubejs:ore_doubling/3x_${i}`)
  })

  console.info(`[Cozy] Ore-Doubling: ${metals.length * 2} Create-Compacting-Rezepte geladen`)
})
