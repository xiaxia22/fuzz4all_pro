# Class OpenFilesEvent

**Source:** `java.desktop\java\awt\desktop\OpenFilesEvent.html`

### Class Description

```java
public final class
OpenFilesEvent

extends
FilesEvent
```

Event sent when the app is asked to open a list of files.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public OpenFilesEvent​(
List
<
File
> files,

String
searchTerm)

Constructs an

OpenFilesEvent

.

**Parameters:**
- files

- the list of files
- searchTerm

- the search term

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
- UnsupportedOperationException

- if Desktop API is not supported on
the current platform

**See Also:**
- Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

### Method Details

#### public
String
getSearchTerm()

Gets the search term. The platform may optionally provide the search
term that was used to find the files. This is for example the case
on Mac OS X, when the files were opened using the Spotlight search
menu or a Finder search window.

This is useful for highlighting the search term in the documents when
they are opened.

**Returns:**
- the search term used to find the files

---

### Additional Sections

#### Class OpenFilesEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.FilesEvent
- - java.awt.desktop.OpenFilesEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.FilesEvent
- - java.awt.desktop.OpenFilesEvent

java.awt.desktop.AppEvent

- java.awt.desktop.FilesEvent
- - java.awt.desktop.OpenFilesEvent

java.awt.desktop.FilesEvent

- java.awt.desktop.OpenFilesEvent

java.awt.desktop.OpenFilesEvent

**All Implemented Interfaces:** Serializable

```java
public final class
OpenFilesEvent

extends
FilesEvent
```

Event sent when the app is asked to open a list of files.

**Since:** 9
**See Also:** OpenFilesHandler.openFiles(java.awt.desktop.OpenFilesEvent)

,

Serialized Form

public final class

OpenFilesEvent

extends

FilesEvent

Event sent when the app is asked to open a list of files.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

OpenFilesEvent

​(

List

<

File

> files,

String

searchTerm)

Constructs an

OpenFilesEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getSearchTerm

()

Gets the search term.

- Methods declared in class java.awt.desktop.

FilesEvent

getFiles

- Methods declared in class java.util.

EventObject

getSource

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

OpenFilesEvent

​(

List

<

File

> files,

String

searchTerm)

Constructs an

OpenFilesEvent

.

---

#### Constructor Summary

Constructs an

OpenFilesEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getSearchTerm

()

Gets the search term.

- Methods declared in class java.awt.desktop.

FilesEvent

getFiles

- Methods declared in class java.util.

EventObject

getSource

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Gets the search term.

Methods declared in class java.awt.desktop.

FilesEvent

getFiles

---

#### Methods declared in class java.awt.desktop. FilesEvent

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- OpenFilesEvent

```java
public OpenFilesEvent​(
List
<
File
> files,

String
searchTerm)
```

Constructs an

OpenFilesEvent

.

**Parameters:** files

- the list of files
**Parameters:** searchTerm

- the search term
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if Desktop API is not supported on
the current platform
**See Also:** Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- getSearchTerm

```java
public
String
getSearchTerm()
```

Gets the search term. The platform may optionally provide the search
term that was used to find the files. This is for example the case
on Mac OS X, when the files were opened using the Spotlight search
menu or a Finder search window.

This is useful for highlighting the search term in the documents when
they are opened.

**Returns:** the search term used to find the files

Constructor Detail

- OpenFilesEvent

```java
public OpenFilesEvent​(
List
<
File
> files,

String
searchTerm)
```

Constructs an

OpenFilesEvent

.

**Parameters:** files

- the list of files
**Parameters:** searchTerm

- the search term
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if Desktop API is not supported on
the current platform
**See Also:** Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

OpenFilesEvent

```java
public OpenFilesEvent​(
List
<
File
> files,

String
searchTerm)
```

Constructs an

OpenFilesEvent

.

**Parameters:** files

- the list of files
**Parameters:** searchTerm

- the search term
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if Desktop API is not supported on
the current platform
**See Also:** Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

#### OpenFilesEvent

public OpenFilesEvent​(

List

<

File

> files,

String

searchTerm)

Constructs an

OpenFilesEvent

.

Method Detail

- getSearchTerm

```java
public
String
getSearchTerm()
```

Gets the search term. The platform may optionally provide the search
term that was used to find the files. This is for example the case
on Mac OS X, when the files were opened using the Spotlight search
menu or a Finder search window.

This is useful for highlighting the search term in the documents when
they are opened.

**Returns:** the search term used to find the files

---

#### Method Detail

getSearchTerm

```java
public
String
getSearchTerm()
```

Gets the search term. The platform may optionally provide the search
term that was used to find the files. This is for example the case
on Mac OS X, when the files were opened using the Spotlight search
menu or a Finder search window.

This is useful for highlighting the search term in the documents when
they are opened.

**Returns:** the search term used to find the files

---

#### getSearchTerm

public

String

getSearchTerm()

Gets the search term. The platform may optionally provide the search
term that was used to find the files. This is for example the case
on Mac OS X, when the files were opened using the Spotlight search
menu or a Finder search window.

This is useful for highlighting the search term in the documents when
they are opened.

This is useful for highlighting the search term in the documents when
they are opened.

---

