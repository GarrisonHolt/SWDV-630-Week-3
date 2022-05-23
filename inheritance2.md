1. Spell is the parent class.
2. Accio and Confundo are child classes.

3. Summoning Charm
   Accio
   Summoning Charm
   No description
   Confundo
   Confundus Charm
   Causes the victim to become confused and befuddled

4. get_description() of Confundo is called. because in study_spell(Confundo()) we are calling study_spell with an object of Confundo and hence the get_description of Confundo is called.

5. we need to add add_description function in Accio class
   add the below function in Accio class
   def get_description(self):
   return "This charm summons an object to the caster, potentially over a significant distance"
