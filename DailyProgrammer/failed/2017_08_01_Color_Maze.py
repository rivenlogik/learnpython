## Color Maze from /r/dailyprogrammer

## Gather inputs ##
# Sequence
sequence = ['R','O','Y','P','O']
# Color map
input_map = '''R R B R R R B P Y G P B B B G P B P P R
B G Y P R P Y Y O R Y P P Y Y R R R P P
B P G R O P Y G R Y Y G P O R Y P B O O
R B B O R P Y O O Y R P B R G R B G P G
R P Y G G G P Y P Y O G B O R Y P B Y O
O R B G B Y B P G R P Y R O G Y G Y R P
B G O O O G B B R O Y Y Y Y P B Y Y G G
P P G B O P Y G B R O G B G R O Y R B R
Y Y P P R B Y B P O O G P Y R P P Y R Y
P O O B B B G O Y G O P B G Y R R Y R B
P P Y R B O O R O R Y B G B G O O P B Y
B B R G Y G P Y G P R R P Y G O O Y R R
O G R Y B P Y O P B R Y B G P G O O B P
R Y G P G G O R Y O O G R G P P Y P B G
P Y P R O O R O Y R P O R Y P Y B B Y R
O Y P G R P R G P O B B R B O B Y Y B P
B Y Y P O Y O Y O R B R G G Y G R G Y G
Y B Y Y G B R R O B O P P O B O R R R P
P O O O P Y G G Y P O G P O B G P R P B
R B B R R R R B B B Y O B G P G G O O Y'''

## Get adjacent colors function
def get_adj_colors(position):
	adj_colors = []
	
	#Grab coordinates out of position
	y = position[0]
	x = position[1]
	print "Grabbing adjacent colors to %d, %d" % (x, y)

	# if on left side
	if x == 0:
		# if at top left corner
		if y == 0:
			adj_colors.append((y,x+1,color_map[y][x+1]))
			adj_colors.append((y+1,x,color_map[y+1][x]))
		# if at bottom left corner
		elif y == len(color_map)-1:
			adj_colors.append((y-1,x,color_map[y-1][x]))
			adj_colors.append((y,x+1,color_map[y][x+1]))
		# otherwise traveling the left side
		else:
			adj_colors.append((y-1,x,color_map[y-1][x]))
			adj_colors.append((y,x+1,color_map[y][x+1]))
			adj_colors.append((y+1,x,color_map[y+1][x]))
	# if on right side
	elif x == len(color_map[y])-1:
		# if at top right corner	
		if y == 0:
			adj_colors.append((y,x-1,color_map[y][x-1]))
			adj_colors.append((y+1,x,color_map[y+1][x]))
		# if at bottom right corner
		elif y == len(color_map)-1:
			adj_colors.append((y,x-1,color_map[y][x-1]))
			adj_colors.append((y-1,x,color_map[y-1][x]))
		# otherwise traveling the right side
		else:
			adj_colors.append((y,x+1,color_map[y][x+1]))
			adj_colors.append((y+1,x,color_map[y+1][x]))
			adj_colors.append((y,x-1,color_map[y][x-1]))
	# In the middle
	else:
		# along the top
		if y == 0:
			adj_colors.append((y,x-1,color_map[y][x-1]))
			adj_colors.append((y,x+1,color_map[y][x+1]))
			adj_colors.append((y,x,color_map[y+1][x]))
		# along the bottom
		elif y == len(color_map)-1:
			adj_colors.append((y,x-1,color_map[y][x-1]))
			adj_colors.append((y-1,x,color_map[y-1][x]))
			adj_colors.append((y,x+1,color_map[y][x+1]))
	# Always returning in order of left, top, right, bottom (as applicable)
	return adj_colors

# Break the color map into lists
color_map_split = input_map.split('\n')
color_map = []
for i in color_map_split:
	color_map.append(i.split(' '))

# Set start position to bottom left of maze
x = 0
y = len(color_map)-1
#print color_map[y][x]

path_list = []
## GET PATH STARTING POSITION ##
## while x < len(x)
while x < len(color_map[y])-1:
	## Get position's color
	current_color = color_map[y][x]
	## Check against start color in sequence
	if current_color == sequence[0]:
	## Add to path list
		path_list.append([y,x])		
	## increment horizontal position x + 1
	x += 1
## END START POINT(S) ##

print path_list

## FIND THE PATH ##
# For each item in path list
for pos in reversed(path_list):
	# Extract coordinates
	y = pos[0]
	x = pos[1]
	# Set current color variable
	current_color = color_map[y][x]
	next_color = ''
	# Figure out where we are in the sequence
	for i in range (0,len(sequence)-1):
		if current_color == sequence[i]:
			# Set the next color variable
			next_color = sequence[i+1]
			print next_color

	# Get adjacent colors
	adj_colors = get_adj_colors(pos)
	print adj_colors
	# Check adjacent colors
	color_found = False
	for color in adj_colors:
		#Check the adjacent color for next color in sequence
		if color[2] == next_color:
			path_list.append((color[0],color[1]))
			color_found = True
			break
	if color_found == False:
		path_list.remove(pos)
	print path_list
# If no adjacent color matches
# Remove position from path list


