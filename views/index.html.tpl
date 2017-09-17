<!DOCTYPE html>
<html>
<head>
  <title>Upload files</title>
  <meta charset="utf-8" />
</head>
<body>
<form action="{{root}}upload" method="post" enctype="multipart/form-data">
  <label>Select a file:
    <input type="file" name="upload" required="required"/>
  </label>
  <input type="submit" value="Upload" />
</form>
<hr />
%if files:
  <ul>
%   for file in sorted(files):
    <li><a href="{{root}}download/{{file}}">{{file}}</a></li>
%   end
  </ul>
%else:
  <p>There are current no uploaded files...</p>
%end
</body>
</html>
