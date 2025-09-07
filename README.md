<h1>Data Setup</h1>

You must run this script from the root of the cloned repo (where the script file is located), so that relative paths resolve correctly. The raster dataset foxlake is provided as a zipped archive (foxlake.zip) inside the data/ folder to keep the repository size manageable. Before running the scripts or notebooks:

<li>Download the repository or clone it locally.</li>

<li>Extract the contents of data/foxlake.zip into the data/ folder so that the full raster folder data/foxlake/ with all .adf and supporting files is available.

Your directory should look like this:

<pre>data/
└── foxlake/
    ├── hdr.adf
    ├── dbldnd.adf
    ├── prj.adf
    ├── sta.adf
    ├── w001001.adf
    ├── w001001x.adf
    ├── log
    └── metadata.xml</pre>
    
<li>Now you can run the scripts and notebooks which reference the raster folder at /data/foxlake.</li>
