// Cozy Farming SMP — Ore-Crushing-Boost
// Erz-Crushing (Crushing Wheels) gibt standardmäßig 1 garantiert + ~75% auf ein zweites.
// Gewünscht: mind. 2 garantiert + 75% auf ein drittes — für ALLE Erz-Crushing-Rezepte.
// Vorgehen: garantierten Crushed-Output auf >=2 anheben, Bonus-Crushed-Output auf chance 0.75.
// Greift nur bei Create-Crushing-Rezepten mit Erz-Input UND crushed_* -Output (Metalle).
// Nicht-Metall-Erze (Diamant/Lapis/Redstone/Kohle/Quarz) bleiben unberührt.

ServerEvents.recipes(event => {
  // Erz-Blöcke (…_ore / #c:ores…) UND Roh-Erze (#c:raw_materials/… / …:raw_iron)
  const isTarget = (ing) => {
    if (!ing) return false
    const tag = ing.tag || ''
    const item = ing.item || ''
    return /(^|[:/])ores?([/]|$)/.test(tag) || /_ore$/.test(item)
      || /raw_materials\//.test(tag) || /(^|:)raw_[a-z]+$/.test(item)
  }
  const isCrushed = (id) => /crushed_/.test(id || '')

  const toRemove = []
  const toAdd = []

  event.forEachRecipe({ type: 'create:crushing' }, (r) => {
    let j
    try { j = JSON.parse(r.json.toString()) } catch (e) { return }

    const ings = j.ingredients || []
    if (!ings.some(isTarget)) return

    const results = j.results || []
    const crushed = results.filter((o) => isCrushed(o.id || o.item))
    if (crushed.length === 0) return

    let mutated = false
    let mainId = null

    // 1) garantierten Crushed-Output (keine/volle chance) auf mind. 2
    crushed.forEach((o) => {
      const ch = (o.chance === undefined) ? 1 : o.chance
      if (ch >= 1) {
        mainId = o.id || o.item
        if ((o.count || 1) < 2) { o.count = 2; mutated = true }
      }
    })
    if (!mainId) mainId = crushed[0].id || crushed[0].item

    // 2) Bonus-Crushed auf 75% (vorhandenen anpassen, sonst neu)
    const bonus = crushed.find((o) => ((o.chance === undefined) ? 1 : o.chance) < 1)
    if (bonus) {
      if (bonus.chance !== 0.75) { bonus.chance = 0.75; mutated = true }
    } else {
      results.push({ chance: 0.75, id: mainId }); mutated = true
    }

    if (mutated) {
      j.results = results
      toRemove.push(r.getOrCreateId().toString())
      toAdd.push(j)
    }
  })

  toRemove.forEach((id) => event.remove({ id: id }))
  toAdd.forEach((j) => event.custom(j))
  console.info(`[Cozy] Ore-Crushing-Boost: ${toAdd.length} Crushing-Rezepte (Erz + Raw) angepasst (>=2 garantiert + 75% auf drittes)`)
})
