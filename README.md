# Plants-Manager
NO WARRANTY, AS IS, NO SUPPORT... unless you are nice


-- Farmware for farmbot --

Load plants with filters and change plants data 


-- Do ---

- Load all plants for current device
- Filter plants with Plant name, Openfarm Slug Name, Plant Age in day range, Meta data key/value
- Loop all filtered plants
    - Update plant data


-- input ---

  {"name": "title", "label": "Title", "value": "-"}
 
-> Title used for description only

  {"name": "id", "label": "Filter by plant id", "value": "*"}

-> Filter by plant id 
-> default : * -> all plants 

  {"name": "pointname", "label": "Filter by plant name", "value": "*"}
  
-> Filter by plant name (equal/Not case sensitive)
-> default : * -> all plant name 

  {"name": "openfarm_slug", "label": "Filter by Openfarm slug name", "value": "*"}

-> Filter by Openfarm type (equal/Not case sensitive)
-> default : * -> all openfarm_slug

  {"name": "age_min_day", "label": "Filter by plant age (minimum days)", "value": "-1"}
  
-> Filter by minimum plant age in days
-> default : -1 -> to be sure with time zone and large range..

  {"name": "age_max_day", "label": "Filter by plant age (maximum days)", "value": "36500"}
  
-> Filter by maximum plant age in days
-> default : 36500 -> a plant of a century...

  {"name": "filter_meta_key", "label": "Filter by meta data : key", "value": "None"}
  
-> Filter by meta data - KEY
-> default : None -> no meta filter

  {"name": "filter_meta_value", "label": "Filter by meta data : value", "value": "None"}
  
-> Filter by meta data - VALUE (equal/Not case sensitive)
-> default : None -> no meta filter

  {"name": "filter_min_x", "label": "Filter by coordinate - Min X", "value": "None"}
  
-> Filter by min coordinate X 
-> default : None -> no filter

  {"name": "filter_max_x", "label": "Filter by coordinate - Max X", "value": "None"}
  
-> Filter by max coordinate X 
-> default : None -> no filter

  {"name": "filter_min_y", "label": "Filter by coordinate - Min Y", "value": "None"}
  
-> Filter by min coordinate Y 
-> default : None -> no filter

  {"name": "filter_max_y", "label": "Filter by coordinate - Max Y", "value": "None"}
  
-> Filter by max coordinate Y 
-> default : None -> no filter

  {"name": "save_name", "label": "Save New Name ", "value": "None"}

-> Change plant with new name
-> default : None -> no change

  {"name": "remove_all_metadata", "label": "Remove All meta data (Yes or No)", "value": "No"}

-> Remove all meta data  
-> default : No -> Keep meta data

  {"name": "save_meta_key", "label": "Save in meta data : key", "value": "None"}
  
-> Save meta data - KEY
-> default : None -> no save meta data

  {"name": "save_meta_value", "label": "Save in meta data : value", "value": "None"}

-> Save meta data - VALUE
-> default : None -> no save meta data

  {"name": "debug", "label": "Debug (0-> Save Data, 1-> Save Data + debug log, 2-> Simulation / log only)", "value": 1}

-> debug mode : 0 -> no farmware debug log, 1 -> farmware debug log, 2 -> simulation : only farmware debug log
-> default : 1 -> move/exec and debug log



