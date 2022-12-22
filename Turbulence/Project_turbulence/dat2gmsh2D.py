# Python Program for quick gmsh grid gen

import string,sys

def convert_pts_togmsh(filename,outputname,startpoint):
	
	# Read in data using this bit
	fin=open(filename, 'r')
	i=0
	x = []; y = []; z = [];
	
	lines = fin.readlines()

	for line in lines:
		# comments indicated by #
		if line[0] != '#' or line[0] != '':
			i=i+1
			data = str.split(line)
			#print(i,data)
			x.append(float(data[0]))
			y.append(float(data[1]))
			z.append(float(0.0)) # so to automatically set to zero, 2D dataset!... fp 20221020 11h40 #z.append(float(data[2]))

			n_lines = int(i)

	# Write data out with this;

	fout = open(outputname,'w')

    # Force GMSH to use OpenCascade engine instead of hte native one, fp 20221020 16h08
	fout.write("SetFactory(\"OpenCASCADE\");\n")

	lc_name = "%s_lc" % filename[0:3] ## characteristic length
	# Format
	# Point(1) = {0, 0, 0, lc};
	#fout.write("%s = 0.005;\n" % lc_name)
	fout.write("%s = 1.0;\n" % lc_name)
	j = startpoint
	for i in range(n_lines):
		outputline  = "Point(%i) = { %8.8f, %8.8f, %8.8f, %s};\n " \
					      % (j,x[i],y[i],z[i],lc_name )
		j = j + 1
		fout.write(outputline)

	# gmsh bspline format	
	# Write out splinefit line
	fout.write("Spline(%i) = {%i:%i,%i};\n" \
		   % (startpoint+1000,startpoint,startpoint+n_lines-1,startpoint)) # modified so to automatically 'close' the profile! fp 20221020

    #Create a loop for the spline
	fout.write(" Line Loop(%i) = {%i};\n" \
		   % (startpoint+2000,startpoint+1000)) 

    #Create a Plane Surface associated to this entity
	fout.write(" Plane Surface(%i) = {%i};\n" \
		   % (startpoint+3000,startpoint+2000)) 
    #Extrude
	fout.write(" Extrude {%i, %i, %s} {Surface{%i}; Layers{1}; Recombine;}\n" \
		   % (0,0,lc_name, startpoint+3000)) 

	fout.close
	fin.close
	
def main():
  inputfile = sys.argv[1]
  outputfile=inputfile.replace(".dat",".geo")
  convert_pts_togmsh(inputfile,outputfile,1000)

if __name__ == "__main__":
    main()
