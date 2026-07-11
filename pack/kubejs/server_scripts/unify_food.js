// Cozy-Integration Phase 1: Basiszutaten vereinheitlichen
// Kanonisches Item ersetzt Duplikate in allen Rezepten; Umtausch-Rezepte für Alt-Items.
ServerEvents.recipes(event => {
  const safe = (id) => { try { return Item.of(id).id !== 'minecraft:air' } catch (e) { return false } }
  if (safe('create:dough') && safe('farmersdelight:wheat_dough')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'create:dough', 'farmersdelight:wheat_dough')
    event.replaceOutput({not: {id: /^cozy:/}}, 'create:dough', 'farmersdelight:wheat_dough')
    event.shapeless('farmersdelight:wheat_dough', ['create:dough']).id('cozy:unify/create_dough')
  }
  if (safe('farm_and_charm:dough') && safe('farmersdelight:wheat_dough')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'farm_and_charm:dough', 'farmersdelight:wheat_dough')
    event.replaceOutput({not: {id: /^cozy:/}}, 'farm_and_charm:dough', 'farmersdelight:wheat_dough')
    event.shapeless('farmersdelight:wheat_dough', ['farm_and_charm:dough']).id('cozy:unify/farm_and_charm_dough')
  }
  if (safe('pamhc2foodcore:doughitem') && safe('farmersdelight:wheat_dough')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'pamhc2foodcore:doughitem', 'farmersdelight:wheat_dough')
    event.replaceOutput({not: {id: /^cozy:/}}, 'pamhc2foodcore:doughitem', 'farmersdelight:wheat_dough')
    event.shapeless('farmersdelight:wheat_dough', ['pamhc2foodcore:doughitem']).id('cozy:unify/pamhc2foodcore_doughitem')
  }
  if (safe('pamhc2foodcore:flouritem') && safe('create:wheat_flour')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'pamhc2foodcore:flouritem', 'create:wheat_flour')
    event.replaceOutput({not: {id: /^cozy:/}}, 'pamhc2foodcore:flouritem', 'create:wheat_flour')
    event.shapeless('create:wheat_flour', ['pamhc2foodcore:flouritem']).id('cozy:unify/pamhc2foodcore_flouritem')
  }
  if (safe('farm_and_charm:flour') && safe('create:wheat_flour')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'farm_and_charm:flour', 'create:wheat_flour')
    event.replaceOutput({not: {id: /^cozy:/}}, 'farm_and_charm:flour', 'create:wheat_flour')
    event.shapeless('create:wheat_flour', ['farm_and_charm:flour']).id('cozy:unify/farm_and_charm_flour')
  }
  if (safe('bountifulfares:flour') && safe('create:wheat_flour')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'bountifulfares:flour', 'create:wheat_flour')
    event.replaceOutput({not: {id: /^cozy:/}}, 'bountifulfares:flour', 'create:wheat_flour')
    event.shapeless('create:wheat_flour', ['bountifulfares:flour']).id('cozy:unify/bountifulfares_flour')
  }
  if (safe('pamhc2foodcore:cheeseitem') && safe('brewinandchewin:flaxen_cheese_wedge')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'pamhc2foodcore:cheeseitem', 'brewinandchewin:flaxen_cheese_wedge')
    event.replaceOutput({not: {id: /^cozy:/}}, 'pamhc2foodcore:cheeseitem', 'brewinandchewin:flaxen_cheese_wedge')
    event.shapeless('brewinandchewin:flaxen_cheese_wedge', ['pamhc2foodcore:cheeseitem']).id('cozy:unify/pamhc2foodcore_cheeseitem')
  }
  if (safe('extradelight:cheese') && safe('brewinandchewin:flaxen_cheese_wedge')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'extradelight:cheese', 'brewinandchewin:flaxen_cheese_wedge')
    event.replaceOutput({not: {id: /^cozy:/}}, 'extradelight:cheese', 'brewinandchewin:flaxen_cheese_wedge')
    event.shapeless('brewinandchewin:flaxen_cheese_wedge', ['extradelight:cheese']).id('cozy:unify/extradelight_cheese')
  }
  if (safe('create_bic_bit:cheese') && safe('brewinandchewin:flaxen_cheese_wedge')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'create_bic_bit:cheese', 'brewinandchewin:flaxen_cheese_wedge')
    event.replaceOutput({not: {id: /^cozy:/}}, 'create_bic_bit:cheese', 'brewinandchewin:flaxen_cheese_wedge')
    event.shapeless('brewinandchewin:flaxen_cheese_wedge', ['create_bic_bit:cheese']).id('cozy:unify/create_bic_bit_cheese')
  }
  if (safe('pizzadelight:cheese') && safe('brewinandchewin:flaxen_cheese_wedge')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'pizzadelight:cheese', 'brewinandchewin:flaxen_cheese_wedge')
    event.replaceOutput({not: {id: /^cozy:/}}, 'pizzadelight:cheese', 'brewinandchewin:flaxen_cheese_wedge')
    event.shapeless('brewinandchewin:flaxen_cheese_wedge', ['pizzadelight:cheese']).id('cozy:unify/pizzadelight_cheese')
  }
  if (safe('pizzadelight:cheese_slice') && safe('expandeddelight:cheese_slice')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'pizzadelight:cheese_slice', 'expandeddelight:cheese_slice')
    event.replaceOutput({not: {id: /^cozy:/}}, 'pizzadelight:cheese_slice', 'expandeddelight:cheese_slice')
    event.shapeless('expandeddelight:cheese_slice', ['pizzadelight:cheese_slice']).id('cozy:unify/pizzadelight_cheese_slice')
  }
  if (safe('farm_and_charm:butter') && safe('extradelight:butter')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'farm_and_charm:butter', 'extradelight:butter')
    event.replaceOutput({not: {id: /^cozy:/}}, 'farm_and_charm:butter', 'extradelight:butter')
    event.shapeless('extradelight:butter', ['farm_and_charm:butter']).id('cozy:unify/farm_and_charm_butter')
  }
  if (safe('pamhc2foodcore:butteritem') && safe('extradelight:butter')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'pamhc2foodcore:butteritem', 'extradelight:butter')
    event.replaceOutput({not: {id: /^cozy:/}}, 'pamhc2foodcore:butteritem', 'extradelight:butter')
    event.shapeless('extradelight:butter', ['pamhc2foodcore:butteritem']).id('cozy:unify/pamhc2foodcore_butteritem')
  }
  if (safe('ratatouille:salt') && safe('expandeddelight:salt')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'ratatouille:salt', 'expandeddelight:salt')
    event.replaceOutput({not: {id: /^cozy:/}}, 'ratatouille:salt', 'expandeddelight:salt')
    event.shapeless('expandeddelight:salt', ['ratatouille:salt']).id('cozy:unify/ratatouille_salt')
  }
  if (safe('meadow:alpine_salt') && safe('expandeddelight:salt')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'meadow:alpine_salt', 'expandeddelight:salt')
    event.replaceOutput({not: {id: /^cozy:/}}, 'meadow:alpine_salt', 'expandeddelight:salt')
    event.shapeless('expandeddelight:salt', ['meadow:alpine_salt']).id('cozy:unify/meadow_alpine_salt')
  }
  if (safe('garnished:crushed_salt') && safe('expandeddelight:salt')) {
    event.replaceInput({not: {id: /^cozy:/}}, 'garnished:crushed_salt', 'expandeddelight:salt')
    event.replaceOutput({not: {id: /^cozy:/}}, 'garnished:crushed_salt', 'expandeddelight:salt')
    event.shapeless('expandeddelight:salt', ['garnished:crushed_salt']).id('cozy:unify/garnished_crushed_salt')
  }
})
