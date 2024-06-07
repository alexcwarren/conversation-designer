# Conversation Designer

Automate Twee code generation for conversation with a user-configured NPC in Twine.

## What's automated and what's not

While the NPC conversation functionality will be largely automated, the aspects of the world will need to be provided by the user.

Yes you'll have to do a little bit of world-building.

All you'll need is the following:

* A list of all location names in your setting
* For each location, a list of other locations that people would be aware of
  * For example, let's say people from the village of "Cobble Hill" don't travel much and are only aware of the local city "Carpenton".
* A list of people of note
* For each person, which locations would be aware of them
* etc.

Once that's complete, the rest of the work is finally done for you!

Here's how it works:

* NPCs are assigned a Role - such as Trader, Farmer, Soldier, etc.
  * This will yield a certain collection of Dialogue from the Dialogue Library
* NPCs are assigned an Interaction type among the following:
  * Argumentative
  * Arrogant
  * Blustering
  * Rude
  * Curious
  * Friendly
  * Honest (default)
  * Hot Tempered
  * Irritable
  * Ponderous
  * Quiet
  * Suspicious

  * This will yield a certain subset of the collection provided earlier as each Role Dialogue has a version for each Interaction type
* NPCs are assigned an Alignment
  * This will help indicate an NPC's Ideals
  * NOTE: In future, this will also be incorporated into an Influencing/Affinity mechanic
* NPCs are assigned two Ideals (based on their Alignment)
  * Ideals will act as tags that will be incorporated into an Influencing/Affinity mechanic later
* NPCs are assigned a Bond and a Flaw/Secret
  * Bonds and Flaws/Secrets will add additional Dialogue for the Player to interact with
  * In future, this might be Dialogue the Player cannot access at first and must use the Influencing/Affinity mechanic to convince the NPC
* NPCs are assigned a Mannerism
  * This will be factored in when processing the final collection of NPC Dialogue
* NPCs will have Inquiries Dialogue where Players are able to ask the NPCs about certain things: Locations, Persons of Interest, Rumors, Groups of People, etc.
  * This Dialogue will come from a specific Dialogue Library that starts out as more of a template and fills out based on the world-building info from earlier
  * TODO

### Dialogue Library Hierarchy

Each Role will have their own set of Dialogue for each Interaction type.

* Role
  * Trader
    * Argumentative
    * Arrogant
    * Blustering
    * Rude
    * Curious
    * Friendly
    * Honest
    * Hot Tempered
    * Irritable
    * Ponderous
    * Quiet
    * Suspicious
  * Farmer
    * Argumentative
    * Arrogant
    * Blustering
    * Rude
    * Curious
    * Friendly
    * Honest
    * Hot Tempered
    * Irritable
    * Ponderous
    * Quiet
    * Suspicious
  * Soldier
    * Argumentative
    * Arrogant
    * Blustering
    * Rude
    * Curious
    * Friendly
    * Honest
    * Hot Tempered
    * Irritable
    * Ponderous
    * Quiet
    * Suspicious

## TODO

* [ ] Start manually writing dialogue for an Honest Trader
  * [ ] Get a pattern of Passage structure figured out
  * [ ] Determine the components of each Passage
    * NPC Dialogue components
    * Player response components
    * What can be variable/randomized?
    * What MUST be present/fixed?
* [ ] Next do an Honest Farmer
  * [ ] Compare what you noted for the Honest Trader to look for what remains the same and what needed to change for the Role
* [ ] Next do an Argumentative Farmer
  * [ ] Compare what you noted for both Honest Trader and Farmer
