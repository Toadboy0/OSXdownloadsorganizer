<html>
<head>
<title>main.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #0033b3;}
.s1 { color: #080808;}
.s2 { color: #8c8c8c; font-style: italic;}
.s3 { color: #067d17;}
.s4 { color: #1750eb;}
</style>
</head>
<body bgcolor="#ffffff">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#c0c0c0" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
main.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">os</span>
<span class="s0">import </span><span class="s1">shutil</span>

<span class="s2"># Assign variable to the file source. /Users/[YourUsername]/</span>
<span class="s1">source_directory = </span><span class="s3">'/Users/peanut/Downloads'</span>

<span class="s2"># Assign variable to the organized folder being created on the desktop. /Users/[YourUsername]/Desktop/[organized_file_name</span>
<span class="s1">base_destination_directory = </span><span class="s3">'/Users/peanut/Desktop/organized_files'</span>

<span class="s2"># Create the file type dictionary. Any file extension can be added. If a file with this extension exists</span>
<span class="s2"># a new folder will be created and the file will be moved to that folder. </span>
<span class="s1">file_type_mapping = {</span>
    <span class="s3">'txt'</span><span class="s1">: </span><span class="s3">'Text Files'</span><span class="s1">,</span>
    <span class="s3">'pdf'</span><span class="s1">: </span><span class="s3">'PDF Files'</span><span class="s1">,</span>
    <span class="s3">'jpg'</span><span class="s1">: </span><span class="s3">'Images'</span><span class="s1">,</span>
    <span class="s3">'png'</span><span class="s1">: </span><span class="s3">'Images'</span><span class="s1">,</span>
    <span class="s3">'mp3'</span><span class="s1">: </span><span class="s3">'Audio'</span><span class="s1">,</span>
    <span class="s3">'mp4'</span><span class="s1">: </span><span class="s3">'Video'</span><span class="s1">,</span>
    <span class="s3">'png'</span><span class="s1">: </span><span class="s3">'Images'</span><span class="s1">,</span>
    <span class="s3">'docx'</span><span class="s1">: </span><span class="s3">'Word Files'</span><span class="s1">,</span>
    <span class="s3">'xlsx'</span><span class="s1">: </span><span class="s3">'Excel Files'</span><span class="s1">,</span>
    <span class="s3">'pptx'</span><span class="s1">: </span><span class="s3">'Powerpoint Files'</span><span class="s1">,</span>
    <span class="s3">'zip'</span><span class="s1">: </span><span class="s3">'Zip Files'</span><span class="s1">,</span>
    <span class="s3">'rar'</span><span class="s1">: </span><span class="s3">'Zip Files'</span><span class="s1">,</span>
    <span class="s3">'py'</span><span class="s1">: </span><span class="s3">'Python Files'</span><span class="s1">,</span>
    <span class="s3">'java'</span><span class="s1">: </span><span class="s3">'Java Files'</span><span class="s1">,</span>
    <span class="s3">'dmg'</span><span class="s1">: </span><span class="s3">'Disk Images'</span><span class="s1">,</span>
    <span class="s3">'pkg'</span><span class="s1">: </span><span class="s3">'Packages'</span><span class="s1">,</span>
    <span class="s3">'json'</span><span class="s1">: </span><span class="s3">'JSON Files'</span><span class="s1">,</span>
    <span class="s3">'csv'</span><span class="s1">: </span><span class="s3">'CSV Files'</span><span class="s1">,</span>
    <span class="s3">'xml'</span><span class="s1">: </span><span class="s3">'XML Files'</span><span class="s1">,</span>
    <span class="s3">'js'</span><span class="s1">: </span><span class="s3">'Javascript Files'</span><span class="s1">,</span>
    <span class="s3">'css'</span><span class="s1">: </span><span class="s3">'CSS Files'</span><span class="s1">,</span>
    <span class="s3">'sql'</span><span class="s1">: </span><span class="s3">'SQL Files'</span><span class="s1">,</span>
    <span class="s3">'db'</span><span class="s1">: </span><span class="s3">'Database Files'</span><span class="s1">,</span>
    <span class="s3">'apk'</span><span class="s1">: </span><span class="s3">'APK Files'</span><span class="s1">,</span>
    <span class="s3">'iso'</span><span class="s1">: </span><span class="s3">'ISO Files'</span><span class="s1">,</span>
    <span class="s3">'torrent'</span><span class="s1">: </span><span class="s3">'Torrent Files'</span><span class="s1">,</span>
    <span class="s2"># Add more file types here if needed</span>
<span class="s1">}</span>

<span class="s2"># Iterative loop for parsing through the source directory</span>
<span class="s0">for </span><span class="s1">filename </span><span class="s0">in </span><span class="s1">os.listdir(source_directory):</span>
    <span class="s1">file_path = os.path.join(source_directory, filename)</span>

    <span class="s2">#  skipping directories</span>
    <span class="s0">if </span><span class="s1">os.path.isdir(file_path):</span>
        <span class="s0">continue</span>

    <span class="s2"># Determine file extension</span>
    <span class="s1">file_extension = os.path.splitext(filename)[</span><span class="s4">1</span><span class="s1">][</span><span class="s4">1</span><span class="s1">:]</span>

    <span class="s2"># Get the folder name from the file_type_mapping dictionary, if not found use 'Others' as the folder name</span>
    <span class="s1">folder_name = file_type_mapping.get(file_extension, </span><span class="s3">'Others'</span><span class="s1">)</span>

    <span class="s2"># Create the destination folder if it doesn't exist</span>
    <span class="s1">destination_folder = os.path.join(base_destination_directory, folder_name)</span>
    <span class="s1">os.makedirs(destination_folder, exist_ok=</span><span class="s0">True</span><span class="s1">)</span>

    <span class="s2"># Move the file to the destination folder</span>
    <span class="s1">shutil.move(file_path, os.path.join(destination_folder, filename))</span>

<span class="s1">print(</span><span class="s3">&quot;File organization complete.&quot;</span><span class="s1">)</span>



</pre>
</body>
</html>