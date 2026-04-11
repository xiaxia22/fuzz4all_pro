# Interface FileVisitor<T>

**Source:** `java.base\java\nio\file\FileVisitor.html`

### Class Description

```java
public interface
FileVisitor<T>
```

A visitor of files. An implementation of this interface is provided to the

Files.walkFileTree

methods to visit each file in
a file tree.

Usage Examples:

Suppose we want to delete a file tree. In that case, each directory should
be deleted after the entries in the directory are deleted.

```java
Path start = ...
Files.walkFileTree(start, new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.delete(file);
return FileVisitResult.CONTINUE;
}
@Override
public FileVisitResult postVisitDirectory(Path dir, IOException e)
throws IOException
{
if (e == null) {
Files.delete(dir);
return FileVisitResult.CONTINUE;
} else {
// directory iteration failed
throw e;
}
}
});
```

Furthermore, suppose we want to copy a file tree to a target location.
In that case, symbolic links should be followed and the target directory
should be created before the entries in the directory are copied.

```java
final Path source = ...
final Path target = ...

Files.walkFileTree(source, EnumSet.of(FileVisitOption.FOLLOW_LINKS), Integer.MAX_VALUE,
new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
throws IOException
{
Path targetdir = target.resolve(source.relativize(dir));
try {
Files.copy(dir, targetdir);
} catch (FileAlreadyExistsException e) {
if (!Files.isDirectory(targetdir))
throw e;
}
return CONTINUE;
}
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.copy(file, target.resolve(source.relativize(file)));
return CONTINUE;
}
});
```

**All Known Implementing Classes:** SimpleFileVisitor

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### FileVisitResult
preVisitDirectory​(
T
dir,

BasicFileAttributes
attrs)
throws
IOException

Invoked for a directory before entries in the directory are visited.

If this method returns

CONTINUE

,
then entries in the directory are visited. If this method returns

SKIP_SUBTREE

or

SKIP_SIBLINGS

then entries in the
directory (and any descendants) will not be visited.

**Parameters:**
- dir

- a reference to the directory
- attrs

- the directory's basic attributes

**Returns:**
- the visit result

**Throws:**
- IOException

- if an I/O error occurs

---

#### FileVisitResult
visitFile​(
T
file,

BasicFileAttributes
attrs)
throws
IOException

Invoked for a file in a directory.

**Parameters:**
- file

- a reference to the file
- attrs

- the file's basic attributes

**Returns:**
- the visit result

**Throws:**
- IOException

- if an I/O error occurs

---

#### FileVisitResult
visitFileFailed​(
T
file,

IOException
exc)
throws
IOException

Invoked for a file that could not be visited. This method is invoked
if the file's attributes could not be read, the file is a directory
that could not be opened, and other reasons.

**Parameters:**
- file

- a reference to the file
- exc

- the I/O exception that prevented the file from being visited

**Returns:**
- the visit result

**Throws:**
- IOException

- if an I/O error occurs

---

#### FileVisitResult
postVisitDirectory​(
T
dir,

IOException
exc)
throws
IOException

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited. This method is also invoked when iteration
of the directory completes prematurely (by a

visitFile

method returning

SKIP_SIBLINGS

,
or an I/O error when iterating over the directory).

**Parameters:**
- dir

- a reference to the directory
- exc

-

null

if the iteration of the directory completes without
an error; otherwise the I/O exception that caused the iteration
of the directory to complete prematurely

**Returns:**
- the visit result

**Throws:**
- IOException

- if an I/O error occurs

---

### Additional Sections

#### Interface FileVisitor<T>

**All Known Implementing Classes:** SimpleFileVisitor

```java
public interface
FileVisitor<T>
```

A visitor of files. An implementation of this interface is provided to the

Files.walkFileTree

methods to visit each file in
a file tree.

Usage Examples:

Suppose we want to delete a file tree. In that case, each directory should
be deleted after the entries in the directory are deleted.

```java
Path start = ...
Files.walkFileTree(start, new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.delete(file);
return FileVisitResult.CONTINUE;
}
@Override
public FileVisitResult postVisitDirectory(Path dir, IOException e)
throws IOException
{
if (e == null) {
Files.delete(dir);
return FileVisitResult.CONTINUE;
} else {
// directory iteration failed
throw e;
}
}
});
```

Furthermore, suppose we want to copy a file tree to a target location.
In that case, symbolic links should be followed and the target directory
should be created before the entries in the directory are copied.

```java
final Path source = ...
final Path target = ...

Files.walkFileTree(source, EnumSet.of(FileVisitOption.FOLLOW_LINKS), Integer.MAX_VALUE,
new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
throws IOException
{
Path targetdir = target.resolve(source.relativize(dir));
try {
Files.copy(dir, targetdir);
} catch (FileAlreadyExistsException e) {
if (!Files.isDirectory(targetdir))
throw e;
}
return CONTINUE;
}
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.copy(file, target.resolve(source.relativize(file)));
return CONTINUE;
}
});
```

**Since:** 1.7

public interface

FileVisitor<T>

A visitor of files. An implementation of this interface is provided to the

Files.walkFileTree

methods to visit each file in
a file tree.

Usage Examples:

Suppose we want to delete a file tree. In that case, each directory should
be deleted after the entries in the directory are deleted.

```java
Path start = ...
Files.walkFileTree(start, new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.delete(file);
return FileVisitResult.CONTINUE;
}
@Override
public FileVisitResult postVisitDirectory(Path dir, IOException e)
throws IOException
{
if (e == null) {
Files.delete(dir);
return FileVisitResult.CONTINUE;
} else {
// directory iteration failed
throw e;
}
}
});
```

Furthermore, suppose we want to copy a file tree to a target location.
In that case, symbolic links should be followed and the target directory
should be created before the entries in the directory are copied.

```java
final Path source = ...
final Path target = ...

Files.walkFileTree(source, EnumSet.of(FileVisitOption.FOLLOW_LINKS), Integer.MAX_VALUE,
new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
throws IOException
{
Path targetdir = target.resolve(source.relativize(dir));
try {
Files.copy(dir, targetdir);
} catch (FileAlreadyExistsException e) {
if (!Files.isDirectory(targetdir))
throw e;
}
return CONTINUE;
}
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.copy(file, target.resolve(source.relativize(file)));
return CONTINUE;
}
});
```

Usage Examples:

Suppose we want to delete a file tree. In that case, each directory should
be deleted after the entries in the directory are deleted.

```java
Path start = ...
Files.walkFileTree(start, new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.delete(file);
return FileVisitResult.CONTINUE;
}
@Override
public FileVisitResult postVisitDirectory(Path dir, IOException e)
throws IOException
{
if (e == null) {
Files.delete(dir);
return FileVisitResult.CONTINUE;
} else {
// directory iteration failed
throw e;
}
}
});
```

Furthermore, suppose we want to copy a file tree to a target location.
In that case, symbolic links should be followed and the target directory
should be created before the entries in the directory are copied.

```java
final Path source = ...
final Path target = ...

Files.walkFileTree(source, EnumSet.of(FileVisitOption.FOLLOW_LINKS), Integer.MAX_VALUE,
new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
throws IOException
{
Path targetdir = target.resolve(source.relativize(dir));
try {
Files.copy(dir, targetdir);
} catch (FileAlreadyExistsException e) {
if (!Files.isDirectory(targetdir))
throw e;
}
return CONTINUE;
}
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.copy(file, target.resolve(source.relativize(file)));
return CONTINUE;
}
});
```

Path start = ...
Files.walkFileTree(start, new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.delete(file);
return FileVisitResult.CONTINUE;
}
@Override
public FileVisitResult postVisitDirectory(Path dir, IOException e)
throws IOException
{
if (e == null) {
Files.delete(dir);
return FileVisitResult.CONTINUE;
} else {
// directory iteration failed
throw e;
}
}
});

Furthermore, suppose we want to copy a file tree to a target location.
In that case, symbolic links should be followed and the target directory
should be created before the entries in the directory are copied.

```java
final Path source = ...
final Path target = ...

Files.walkFileTree(source, EnumSet.of(FileVisitOption.FOLLOW_LINKS), Integer.MAX_VALUE,
new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
throws IOException
{
Path targetdir = target.resolve(source.relativize(dir));
try {
Files.copy(dir, targetdir);
} catch (FileAlreadyExistsException e) {
if (!Files.isDirectory(targetdir))
throw e;
}
return CONTINUE;
}
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.copy(file, target.resolve(source.relativize(file)));
return CONTINUE;
}
});
```

final Path source = ...
final Path target = ...

Files.walkFileTree(source, EnumSet.of(FileVisitOption.FOLLOW_LINKS), Integer.MAX_VALUE,
new SimpleFileVisitor<Path>() {
@Override
public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs)
throws IOException
{
Path targetdir = target.resolve(source.relativize(dir));
try {
Files.copy(dir, targetdir);
} catch (FileAlreadyExistsException e) {
if (!Files.isDirectory(targetdir))
throw e;
}
return CONTINUE;
}
@Override
public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
throws IOException
{
Files.copy(file, target.resolve(source.relativize(file)));
return CONTINUE;
}
});

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

FileVisitResult

postVisitDirectory

​(

T

dir,

IOException

exc)

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

FileVisitResult

preVisitDirectory

​(

T

dir,

BasicFileAttributes

attrs)

Invoked for a directory before entries in the directory are visited.

FileVisitResult

visitFile

​(

T

file,

BasicFileAttributes

attrs)

Invoked for a file in a directory.

FileVisitResult

visitFileFailed

​(

T

file,

IOException

exc)

Invoked for a file that could not be visited.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

FileVisitResult

postVisitDirectory

​(

T

dir,

IOException

exc)

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

FileVisitResult

preVisitDirectory

​(

T

dir,

BasicFileAttributes

attrs)

Invoked for a directory before entries in the directory are visited.

FileVisitResult

visitFile

​(

T

file,

BasicFileAttributes

attrs)

Invoked for a file in a directory.

FileVisitResult

visitFileFailed

​(

T

file,

IOException

exc)

Invoked for a file that could not be visited.

---

#### Method Summary

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited.

Invoked for a directory before entries in the directory are visited.

Invoked for a file in a directory.

Invoked for a file that could not be visited.

============ METHOD DETAIL ==========

- Method Detail

- preVisitDirectory

```java
FileVisitResult
preVisitDirectory​(
T
dir,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a directory before entries in the directory are visited.

If this method returns

CONTINUE

,
then entries in the directory are visited. If this method returns

SKIP_SUBTREE

or

SKIP_SIBLINGS

then entries in the
directory (and any descendants) will not be visited.

**Parameters:** dir

- a reference to the directory
**Parameters:** attrs

- the directory's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- visitFile

```java
FileVisitResult
visitFile​(
T
file,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a file in a directory.

**Parameters:** file

- a reference to the file
**Parameters:** attrs

- the file's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- visitFileFailed

```java
FileVisitResult
visitFileFailed​(
T
file,

IOException
exc)
throws
IOException
```

Invoked for a file that could not be visited. This method is invoked
if the file's attributes could not be read, the file is a directory
that could not be opened, and other reasons.

**Parameters:** file

- a reference to the file
**Parameters:** exc

- the I/O exception that prevented the file from being visited
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- postVisitDirectory

```java
FileVisitResult
postVisitDirectory​(
T
dir,

IOException
exc)
throws
IOException
```

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited. This method is also invoked when iteration
of the directory completes prematurely (by a

visitFile

method returning

SKIP_SIBLINGS

,
or an I/O error when iterating over the directory).

**Parameters:** dir

- a reference to the directory
**Parameters:** exc

-

null

if the iteration of the directory completes without
an error; otherwise the I/O exception that caused the iteration
of the directory to complete prematurely
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

Method Detail

- preVisitDirectory

```java
FileVisitResult
preVisitDirectory​(
T
dir,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a directory before entries in the directory are visited.

If this method returns

CONTINUE

,
then entries in the directory are visited. If this method returns

SKIP_SUBTREE

or

SKIP_SIBLINGS

then entries in the
directory (and any descendants) will not be visited.

**Parameters:** dir

- a reference to the directory
**Parameters:** attrs

- the directory's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- visitFile

```java
FileVisitResult
visitFile​(
T
file,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a file in a directory.

**Parameters:** file

- a reference to the file
**Parameters:** attrs

- the file's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- visitFileFailed

```java
FileVisitResult
visitFileFailed​(
T
file,

IOException
exc)
throws
IOException
```

Invoked for a file that could not be visited. This method is invoked
if the file's attributes could not be read, the file is a directory
that could not be opened, and other reasons.

**Parameters:** file

- a reference to the file
**Parameters:** exc

- the I/O exception that prevented the file from being visited
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

- postVisitDirectory

```java
FileVisitResult
postVisitDirectory​(
T
dir,

IOException
exc)
throws
IOException
```

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited. This method is also invoked when iteration
of the directory completes prematurely (by a

visitFile

method returning

SKIP_SIBLINGS

,
or an I/O error when iterating over the directory).

**Parameters:** dir

- a reference to the directory
**Parameters:** exc

-

null

if the iteration of the directory completes without
an error; otherwise the I/O exception that caused the iteration
of the directory to complete prematurely
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### Method Detail

preVisitDirectory

```java
FileVisitResult
preVisitDirectory​(
T
dir,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a directory before entries in the directory are visited.

If this method returns

CONTINUE

,
then entries in the directory are visited. If this method returns

SKIP_SUBTREE

or

SKIP_SIBLINGS

then entries in the
directory (and any descendants) will not be visited.

**Parameters:** dir

- a reference to the directory
**Parameters:** attrs

- the directory's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### preVisitDirectory

FileVisitResult

preVisitDirectory​(

T

dir,

BasicFileAttributes

attrs)
throws

IOException

Invoked for a directory before entries in the directory are visited.

If this method returns

CONTINUE

,
then entries in the directory are visited. If this method returns

SKIP_SUBTREE

or

SKIP_SIBLINGS

then entries in the
directory (and any descendants) will not be visited.

If this method returns

CONTINUE

,
then entries in the directory are visited. If this method returns

SKIP_SUBTREE

or

SKIP_SIBLINGS

then entries in the
directory (and any descendants) will not be visited.

visitFile

```java
FileVisitResult
visitFile​(
T
file,

BasicFileAttributes
attrs)
throws
IOException
```

Invoked for a file in a directory.

**Parameters:** file

- a reference to the file
**Parameters:** attrs

- the file's basic attributes
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### visitFile

FileVisitResult

visitFile​(

T

file,

BasicFileAttributes

attrs)
throws

IOException

Invoked for a file in a directory.

visitFileFailed

```java
FileVisitResult
visitFileFailed​(
T
file,

IOException
exc)
throws
IOException
```

Invoked for a file that could not be visited. This method is invoked
if the file's attributes could not be read, the file is a directory
that could not be opened, and other reasons.

**Parameters:** file

- a reference to the file
**Parameters:** exc

- the I/O exception that prevented the file from being visited
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### visitFileFailed

FileVisitResult

visitFileFailed​(

T

file,

IOException

exc)
throws

IOException

Invoked for a file that could not be visited. This method is invoked
if the file's attributes could not be read, the file is a directory
that could not be opened, and other reasons.

postVisitDirectory

```java
FileVisitResult
postVisitDirectory​(
T
dir,

IOException
exc)
throws
IOException
```

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited. This method is also invoked when iteration
of the directory completes prematurely (by a

visitFile

method returning

SKIP_SIBLINGS

,
or an I/O error when iterating over the directory).

**Parameters:** dir

- a reference to the directory
**Parameters:** exc

-

null

if the iteration of the directory completes without
an error; otherwise the I/O exception that caused the iteration
of the directory to complete prematurely
**Returns:** the visit result
**Throws:** IOException

- if an I/O error occurs

---

#### postVisitDirectory

FileVisitResult

postVisitDirectory​(

T

dir,

IOException

exc)
throws

IOException

Invoked for a directory after entries in the directory, and all of their
descendants, have been visited. This method is also invoked when iteration
of the directory completes prematurely (by a

visitFile

method returning

SKIP_SIBLINGS

,
or an I/O error when iterating over the directory).

---

