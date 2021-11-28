"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from collections import defaultdict
from evennia.utils.utils import list_to_string

class AlpacasRoom(DefaultRoom):
    def return_appearance(self, looker, **kwargs):
        """
        ALPACAS
        =======
        Copied from Evennia's default object. It should behave just 
        like the default one does, except it will also provide additional
        messages and hooks meant for providing ALPACASclient with all
        the details it needs to render the game. 

        Evennia
        =======
        This formats a description. It is the hook a 'look' command
        should call.
        Args:
            looker (Object): Object doing the looking.
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call (unused by default).
        """
        if not looker:
            return ""
        # get and identify all objects
        visible = (con for con in self.contents if con != looker and con.access(looker, "view"))
        exits, users, things = [], [], defaultdict(list)

        # Blank dictionary for ALPACASclient message
        render_list = []
        
        for con in visible:
            key = con.get_display_name(looker)
            if con.destination:
                exits.append(key)
                con_type = "exit"
            elif con.has_account:
                users.append("|c%s|n" % key)
                con_type = "user"
            else:
                con_type = "thing"
                # things can be pluralized
                things[key].append(con)
            con_entry = {
                "name" : key,
                "id" : con.id,
                "obj_type" : con_type,
                "sprite" : con.db.sprite_file
            }
            render_list.append(con_entry)
            
        # get description, build string
        string = "|c%s|n\n" % self.get_display_name(looker)
        desc = self.db.desc
        if desc:
            string += "%s" % desc
        if exits:
            string += "\n|wExits:|n " + list_to_string(exits)
        if users or things:
            # handle pluralization of things (never pluralize users)
            thing_strings = []
            for key, itemlist in sorted(things.items()):
                nitem = len(itemlist)
                if nitem == 1:
                    key, _ = itemlist[0].get_numbered_name(nitem, looker, key=key)
                else:
                    key = [item.get_numbered_name(nitem, looker, key=key)[1] for item in itemlist][
                        0
                    ]
                thing_strings.append(key)

            string += "\n|wYou see:|n " + list_to_string(users + thing_strings)

        return {"description":string, "render_list":render_list}

class Room(AlpacasRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    pass
