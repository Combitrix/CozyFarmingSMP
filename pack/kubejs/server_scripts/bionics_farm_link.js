// Cozy-Integration Phase 3: Bionics-Roboter brauchen Farm-Biomasse
// Motoren laufen mit Biomasse-Pellets statt Kohle -> Landwirtschaft treibt die Robotik an.
ServerEvents.recipes(event => {
  event.replaceInput({mod: 'createbionics'}, 'minecraft:coal', 'createaddition:biomass_pellet')
})
