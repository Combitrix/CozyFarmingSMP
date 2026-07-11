// Cozy-Integration Phase 2: Create-Maschinen als zentrale Food-Verarbeitung
ServerEvents.recipes(event => {
  event.recipes.create.milling('create:wheat_flour', 'pamhc2crops:barleyitem').id('cozy:milling/pamhc2crops_barleyitem')
  event.recipes.create.milling('create:wheat_flour', 'pamhc2crops:oatsitem').id('cozy:milling/pamhc2crops_oatsitem')
  event.recipes.create.milling('create:wheat_flour', 'pamhc2crops:ryeitem').id('cozy:milling/pamhc2crops_ryeitem')
  event.recipes.create.milling('create:wheat_flour', 'farm_and_charm:barley').id('cozy:milling/farm_and_charm_barley')
  event.recipes.create.milling('create:wheat_flour', 'farm_and_charm:oat').id('cozy:milling/farm_and_charm_oat')
  // Milch + Salz -> Käse (erhitzt)
  event.recipes.create.mixing(['2x brewinandchewin:flaxen_cheese_wedge'], [Fluid.of('minecraft:milk', 1000), 'expandeddelight:salt']).heated().id('cozy:mixing/cheese')
  // Milch -> Butter
  event.recipes.create.compacting(['extradelight:butter'], [Fluid.of('minecraft:milk', 500)]).id('cozy:compacting/butter')
})
