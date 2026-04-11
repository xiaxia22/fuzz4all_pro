# Class HTMLEditorKit.HTMLFactory

**Source:** `java.desktop\javax\swing\text\html\HTMLEditorKit.HTMLFactory.html`

### Class Description

```java
public static class
HTMLEditorKit.HTMLFactory

extends
Object

implements
ViewFactory
```

A factory to build views for HTML. The following
table describes what this factory will build by
default.

Describes the tag and view created by this factory by default

Tag

View created

HTML.Tag.CONTENT

InlineView

HTML.Tag.IMPLIED

javax.swing.text.html.ParagraphView

HTML.Tag.P

javax.swing.text.html.ParagraphView

HTML.Tag.H1

javax.swing.text.html.ParagraphView

HTML.Tag.H2

javax.swing.text.html.ParagraphView

HTML.Tag.H3

javax.swing.text.html.ParagraphView

HTML.Tag.H4

javax.swing.text.html.ParagraphView

HTML.Tag.H5

javax.swing.text.html.ParagraphView

HTML.Tag.H6

javax.swing.text.html.ParagraphView

HTML.Tag.DT

javax.swing.text.html.ParagraphView

HTML.Tag.MENU

ListView

HTML.Tag.DIR

ListView

HTML.Tag.UL

ListView

HTML.Tag.OL

ListView

HTML.Tag.LI

BlockView

HTML.Tag.DL

BlockView

HTML.Tag.DD

BlockView

HTML.Tag.BODY

BlockView

HTML.Tag.HTML

BlockView

HTML.Tag.CENTER

BlockView

HTML.Tag.DIV

BlockView

HTML.Tag.BLOCKQUOTE

BlockView

HTML.Tag.PRE

BlockView

HTML.Tag.BLOCKQUOTE

BlockView

HTML.Tag.PRE

BlockView

HTML.Tag.IMG

ImageView

HTML.Tag.HR

HRuleView

HTML.Tag.BR

BRView

HTML.Tag.TABLE

javax.swing.text.html.TableView

HTML.Tag.INPUT

FormView

HTML.Tag.SELECT

FormView

HTML.Tag.TEXTAREA

FormView

HTML.Tag.OBJECT

ObjectView

HTML.Tag.FRAMESET

FrameSetView

HTML.Tag.FRAME

FrameView

**All Implemented Interfaces:** ViewFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public HTMLFactory()

*No description found.*

---

### Method Details

#### public
View
create​(
Element
elem)

Creates a view from an element.

**Specified by:**
- create

in interface

ViewFactory

**Parameters:**
- elem

- the element

**Returns:**
- the view

**See Also:**
- View

---

### Additional Sections

#### Class HTMLEditorKit.HTMLFactory

java.lang.Object

- javax.swing.text.html.HTMLEditorKit.HTMLFactory

javax.swing.text.html.HTMLEditorKit.HTMLFactory

**All Implemented Interfaces:** ViewFactory

**Enclosing class:** HTMLEditorKit

```java
public static class
HTMLEditorKit.HTMLFactory

extends
Object

implements
ViewFactory
```

A factory to build views for HTML. The following
table describes what this factory will build by
default.

Describes the tag and view created by this factory by default

Tag

View created

HTML.Tag.CONTENT

InlineView

HTML.Tag.IMPLIED

javax.swing.text.html.ParagraphView

HTML.Tag.P

javax.swing.text.html.ParagraphView

HTML.Tag.H1

javax.swing.text.html.ParagraphView

HTML.Tag.H2

javax.swing.text.html.ParagraphView

HTML.Tag.H3

javax.swing.text.html.ParagraphView

HTML.Tag.H4

javax.swing.text.html.ParagraphView

HTML.Tag.H5

javax.swing.text.html.ParagraphView

HTML.Tag.H6

javax.swing.text.html.ParagraphView

HTML.Tag.DT

javax.swing.text.html.ParagraphView

HTML.Tag.MENU

ListView

HTML.Tag.DIR

ListView

HTML.Tag.UL

ListView

HTML.Tag.OL

ListView

HTML.Tag.LI

BlockView

HTML.Tag.DL

BlockView

HTML.Tag.DD

BlockView

HTML.Tag.BODY

BlockView

HTML.Tag.HTML

BlockView

HTML.Tag.CENTER

BlockView

HTML.Tag.DIV

BlockView

HTML.Tag.BLOCKQUOTE

BlockView

HTML.Tag.PRE

BlockView

HTML.Tag.BLOCKQUOTE

BlockView

HTML.Tag.PRE

BlockView

HTML.Tag.IMG

ImageView

HTML.Tag.HR

HRuleView

HTML.Tag.BR

BRView

HTML.Tag.TABLE

javax.swing.text.html.TableView

HTML.Tag.INPUT

FormView

HTML.Tag.SELECT

FormView

HTML.Tag.TEXTAREA

FormView

HTML.Tag.OBJECT

ObjectView

HTML.Tag.FRAMESET

FrameSetView

HTML.Tag.FRAME

FrameView

public static class

HTMLEditorKit.HTMLFactory

extends

Object

implements

ViewFactory

A factory to build views for HTML. The following
table describes what this factory will build by
default.

Describes the tag and view created by this factory by default

Tag

View created

HTML.Tag.CONTENT

InlineView

HTML.Tag.IMPLIED

javax.swing.text.html.ParagraphView

HTML.Tag.P

javax.swing.text.html.ParagraphView

HTML.Tag.H1

javax.swing.text.html.ParagraphView

HTML.Tag.H2

javax.swing.text.html.ParagraphView

HTML.Tag.H3

javax.swing.text.html.ParagraphView

HTML.Tag.H4

javax.swing.text.html.ParagraphView

HTML.Tag.H5

javax.swing.text.html.ParagraphView

HTML.Tag.H6

javax.swing.text.html.ParagraphView

HTML.Tag.DT

javax.swing.text.html.ParagraphView

HTML.Tag.MENU

ListView

HTML.Tag.DIR

ListView

HTML.Tag.UL

ListView

HTML.Tag.OL

ListView

HTML.Tag.LI

BlockView

HTML.Tag.DL

BlockView

HTML.Tag.DD

BlockView

HTML.Tag.BODY

BlockView

HTML.Tag.HTML

BlockView

HTML.Tag.CENTER

BlockView

HTML.Tag.DIV

BlockView

HTML.Tag.BLOCKQUOTE

BlockView

HTML.Tag.PRE

BlockView

HTML.Tag.BLOCKQUOTE

BlockView

HTML.Tag.PRE

BlockView

HTML.Tag.IMG

ImageView

HTML.Tag.HR

HRuleView

HTML.Tag.BR

BRView

HTML.Tag.TABLE

javax.swing.text.html.TableView

HTML.Tag.INPUT

FormView

HTML.Tag.SELECT

FormView

HTML.Tag.TEXTAREA

FormView

HTML.Tag.OBJECT

ObjectView

HTML.Tag.FRAMESET

FrameSetView

HTML.Tag.FRAME

FrameView

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HTMLFactory

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

View

create

​(

Element

elem)

Creates a view from an element.

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

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

HTMLFactory

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

View

create

​(

Element

elem)

Creates a view from an element.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Creates a view from an element.

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

toString

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

- HTMLFactory

```java
public HTMLFactory()
```

============ METHOD DETAIL ==========

- Method Detail

- create

```java
public
View
create​(
Element
elem)
```

Creates a view from an element.

**Specified by:** create

in interface

ViewFactory
**Parameters:** elem

- the element
**Returns:** the view
**See Also:** View

Constructor Detail

- HTMLFactory

```java
public HTMLFactory()
```

---

#### Constructor Detail

HTMLFactory

```java
public HTMLFactory()
```

---

#### HTMLFactory

public HTMLFactory()

Method Detail

- create

```java
public
View
create​(
Element
elem)
```

Creates a view from an element.

**Specified by:** create

in interface

ViewFactory
**Parameters:** elem

- the element
**Returns:** the view
**See Also:** View

---

#### Method Detail

create

```java
public
View
create​(
Element
elem)
```

Creates a view from an element.

**Specified by:** create

in interface

ViewFactory
**Parameters:** elem

- the element
**Returns:** the view
**See Also:** View

---

#### create

public

View

create​(

Element

elem)

Creates a view from an element.

---

