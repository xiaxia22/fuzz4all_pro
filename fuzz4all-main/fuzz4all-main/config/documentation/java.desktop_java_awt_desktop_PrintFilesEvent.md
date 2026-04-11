# Class PrintFilesEvent

**Source:** `java.desktop\java\awt\desktop\PrintFilesEvent.html`

### Class Description

```java
public final class
PrintFilesEvent

extends
FilesEvent
```

Event sent when the app is asked to print a list of files.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrintFilesEvent​(
List
<
File
> files)

Constructs a

PrintFilesEvent

.

**Parameters:**
- files

- the list of files

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

*No entries found.*

### Additional Sections

#### Class PrintFilesEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.FilesEvent
- - java.awt.desktop.PrintFilesEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.FilesEvent
- - java.awt.desktop.PrintFilesEvent

java.awt.desktop.AppEvent

- java.awt.desktop.FilesEvent
- - java.awt.desktop.PrintFilesEvent

java.awt.desktop.FilesEvent

- java.awt.desktop.PrintFilesEvent

java.awt.desktop.PrintFilesEvent

**All Implemented Interfaces:** Serializable

```java
public final class
PrintFilesEvent

extends
FilesEvent
```

Event sent when the app is asked to print a list of files.

**Since:** 9
**See Also:** PrintFilesHandler.printFiles(PrintFilesEvent)

,

Serialized Form

public final class

PrintFilesEvent

extends

FilesEvent

Event sent when the app is asked to print a list of files.

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

PrintFilesEvent

​(

List

<

File

> files)

Constructs a

PrintFilesEvent

.

========== METHOD SUMMARY ===========

- Method Summary

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

PrintFilesEvent

​(

List

<

File

> files)

Constructs a

PrintFilesEvent

.

---

#### Constructor Summary

Constructs a

PrintFilesEvent

.

Method Summary

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

- PrintFilesEvent

```java
public PrintFilesEvent​(
List
<
File
> files)
```

Constructs a

PrintFilesEvent

.

**Parameters:** files

- the list of files
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

Constructor Detail

- PrintFilesEvent

```java
public PrintFilesEvent​(
List
<
File
> files)
```

Constructs a

PrintFilesEvent

.

**Parameters:** files

- the list of files
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

PrintFilesEvent

```java
public PrintFilesEvent​(
List
<
File
> files)
```

Constructs a

PrintFilesEvent

.

**Parameters:** files

- the list of files
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

#### PrintFilesEvent

public PrintFilesEvent​(

List

<

File

> files)

Constructs a

PrintFilesEvent

.

---

