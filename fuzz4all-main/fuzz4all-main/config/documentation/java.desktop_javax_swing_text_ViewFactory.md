# Interface ViewFactory

**Source:** `java.desktop\javax\swing\text\ViewFactory.html`

### Class Description

```java
public interface
ViewFactory
```

A factory to create a view of some portion of document subject.
This is intended to enable customization of how views get
mapped over a document model.

**All Known Implementing Classes:** BasicEditorPaneUI

,

BasicFormattedTextFieldUI

,

BasicPasswordFieldUI

,

BasicTextAreaUI

,

BasicTextFieldUI

,

BasicTextPaneUI

,

BasicTextUI

,

DefaultTextUI

,

HTMLEditorKit.HTMLFactory

,

MetalTextFieldUI

,

SynthEditorPaneUI

,

SynthFormattedTextFieldUI

,

SynthPasswordFieldUI

,

SynthTextAreaUI

,

SynthTextFieldUI

,

SynthTextPaneUI

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### View
create​(
Element
elem)

Creates a view from the given structural element of a
document.

**Parameters:**
- elem

- the piece of the document to build a view of

**Returns:**
- the view

**See Also:**
- View

---

### Additional Sections

#### Interface ViewFactory

**All Known Implementing Classes:** BasicEditorPaneUI

,

BasicFormattedTextFieldUI

,

BasicPasswordFieldUI

,

BasicTextAreaUI

,

BasicTextFieldUI

,

BasicTextPaneUI

,

BasicTextUI

,

DefaultTextUI

,

HTMLEditorKit.HTMLFactory

,

MetalTextFieldUI

,

SynthEditorPaneUI

,

SynthFormattedTextFieldUI

,

SynthPasswordFieldUI

,

SynthTextAreaUI

,

SynthTextFieldUI

,

SynthTextPaneUI

```java
public interface
ViewFactory
```

A factory to create a view of some portion of document subject.
This is intended to enable customization of how views get
mapped over a document model.

public interface

ViewFactory

A factory to create a view of some portion of document subject.
This is intended to enable customization of how views get
mapped over a document model.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

View

create

​(

Element

elem)

Creates a view from the given structural element of a
document.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

View

create

​(

Element

elem)

Creates a view from the given structural element of a
document.

---

#### Method Summary

Creates a view from the given structural element of a
document.

============ METHOD DETAIL ==========

- Method Detail

- create

```java
View
create​(
Element
elem)
```

Creates a view from the given structural element of a
document.

**Parameters:** elem

- the piece of the document to build a view of
**Returns:** the view
**See Also:** View

Method Detail

- create

```java
View
create​(
Element
elem)
```

Creates a view from the given structural element of a
document.

**Parameters:** elem

- the piece of the document to build a view of
**Returns:** the view
**See Also:** View

---

#### Method Detail

create

```java
View
create​(
Element
elem)
```

Creates a view from the given structural element of a
document.

**Parameters:** elem

- the piece of the document to build a view of
**Returns:** the view
**See Also:** View

---

#### create

View

create​(

Element

elem)

Creates a view from the given structural element of a
document.

---

