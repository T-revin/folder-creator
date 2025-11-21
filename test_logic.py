import pandas as pd
import os

def generate_paths(excel_file):
    df = pd.read_excel(excel_file)
    
    # Set of all valid paths (tuples of segments)
    # We start empty.
    all_paths = set()
    
    # Map of depth -> level name (generic name from header)
    level_names = {}
    
    for col_idx, col_name in enumerate(df.columns):
        # Parse header
        parts = str(col_name).strip().split('/')
        target_depth = len(parts) - 1
        new_level_name = parts[-1]
        
        # Register level name if not exists (or maybe overwrite? First one sets the standard?)
        # Assuming the first time we see a depth, that's the generic name.
        if target_depth not in level_names:
            level_names[target_depth] = new_level_name
            
        # Get values, filter NaNs
        values = df[col_name].dropna().astype(str).tolist()
        values = [v.strip() for v in values if v.strip()]
        
        if not values:
            continue
            
        if target_depth == 0:
            # Root level
            for v in values:
                all_paths.add((v,))
        else:
            # Extending existing paths
            # We need to find paths of length == target_depth (i.e. parents)
            # And check if they match the constraints from the header
            
            # Constraints: parts[0] to parts[target_depth-1]
            constraints = parts[:-1]
            
            # Identify candidates
            candidates = [p for p in all_paths if len(p) == target_depth]
            
            for parent_path in candidates:
                match = True
                for i, constraint in enumerate(constraints):
                    # Check constraint at depth i
                    # If constraint matches the generic level name, it's a wildcard
                    # If constraint is different, it must match the path segment exactly
                    
                    generic_name = level_names.get(i)
                    path_segment = parent_path[i]
                    
                    if constraint == generic_name:
                        # Wildcard match
                        continue
                    elif constraint == path_segment:
                        # Literal match
                        continue
                    else:
                        # Mismatch
                        match = False
                        break
                
                if match:
                    # Add new children
                    for v in values:
                        new_path = parent_path + (v,)
                        all_paths.add(new_path)
                        
    return sorted(list(all_paths))

if __name__ == "__main__":
    excel_file = r"C:\Users\User\Downloads\test_nest_v2.xlsx"
    paths = generate_paths(excel_file)
    print(f"Generated {len(paths)} paths:")
    for p in paths:
        print("/".join(p))
