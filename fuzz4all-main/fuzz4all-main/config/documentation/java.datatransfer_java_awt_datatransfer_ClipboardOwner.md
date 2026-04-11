# Interface ClipboardOwner

**Source:** `java.datatransfer\java\awt\datatransfer\ClipboardOwner.html`

### Class Description

```java
public interface
ClipboardOwner
```

Defines the interface for classes that will provide data to a clipboard. An
instance of this interface becomes the owner of the contents of a clipboard
(clipboard owner) if it is passed as an argument to

Clipboard.setContents(java.awt.datatransfer.Transferable, java.awt.datatransfer.ClipboardOwner)

method of the clipboard and this method returns
successfully. The instance remains the clipboard owner until another
application or another object within this application asserts ownership of
this clipboard.

**All Known Implementing Classes:** StringSelection

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void lostOwnership​(
Clipboard
clipboard,

Transferable
contents)

Notifies this object that it is no longer the clipboard owner. This
method will be called when another application or another object within
this application asserts ownership of the clipboard.

**Parameters:**
- clipboard

- the clipboard that is no longer owned
- contents

- the contents which this owner had placed on the

clipboard

---

### Additional Sections

#### Interface ClipboardOwner

**All Known Implementing Classes:** StringSelection

```java
public interface
ClipboardOwner
```

Defines the interface for classes that will provide data to a clipboard. An
instance of this interface becomes the owner of the contents of a clipboard
(clipboard owner) if it is passed as an argument to

Clipboard.setContents(java.awt.datatransfer.Transferable, java.awt.datatransfer.ClipboardOwner)

method of the clipboard and this method returns
successfully. The instance remains the clipboard owner until another
application or another object within this application asserts ownership of
this clipboard.

**Since:** 1.1
**See Also:** Clipboard

public interface

ClipboardOwner

Defines the interface for classes that will provide data to a clipboard. An
instance of this interface becomes the owner of the contents of a clipboard
(clipboard owner) if it is passed as an argument to

Clipboard.setContents(java.awt.datatransfer.Transferable, java.awt.datatransfer.ClipboardOwner)

method of the clipboard and this method returns
successfully. The instance remains the clipboard owner until another
application or another object within this application asserts ownership of
this clipboard.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

lostOwnership

​(

Clipboard

clipboard,

Transferable

contents)

Notifies this object that it is no longer the clipboard owner.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

lostOwnership

​(

Clipboard

clipboard,

Transferable

contents)

Notifies this object that it is no longer the clipboard owner.

---

#### Method Summary

Notifies this object that it is no longer the clipboard owner.

============ METHOD DETAIL ==========

- Method Detail

- lostOwnership

```java
void lostOwnership​(
Clipboard
clipboard,

Transferable
contents)
```

Notifies this object that it is no longer the clipboard owner. This
method will be called when another application or another object within
this application asserts ownership of the clipboard.

**Parameters:** clipboard

- the clipboard that is no longer owned
**Parameters:** contents

- the contents which this owner had placed on the

clipboard

Method Detail

- lostOwnership

```java
void lostOwnership​(
Clipboard
clipboard,

Transferable
contents)
```

Notifies this object that it is no longer the clipboard owner. This
method will be called when another application or another object within
this application asserts ownership of the clipboard.

**Parameters:** clipboard

- the clipboard that is no longer owned
**Parameters:** contents

- the contents which this owner had placed on the

clipboard

---

#### Method Detail

lostOwnership

```java
void lostOwnership​(
Clipboard
clipboard,

Transferable
contents)
```

Notifies this object that it is no longer the clipboard owner. This
method will be called when another application or another object within
this application asserts ownership of the clipboard.

**Parameters:** clipboard

- the clipboard that is no longer owned
**Parameters:** contents

- the contents which this owner had placed on the

clipboard

---

#### lostOwnership

void lostOwnership​(

Clipboard

clipboard,

Transferable

contents)

Notifies this object that it is no longer the clipboard owner. This
method will be called when another application or another object within
this application asserts ownership of the clipboard.

---

