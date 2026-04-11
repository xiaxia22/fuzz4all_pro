# Class NavigationFilter

**Source:** `java.desktop\javax\swing\text\NavigationFilter.html`

### Class Description

```java
public class
NavigationFilter

extends
Object
```

NavigationFilter

can be used to restrict where the cursor can
be positioned. When the default cursor positioning actions attempt to
reposition the cursor they will call into the

NavigationFilter

, assuming
the

JTextComponent

has a non-null

NavigationFilter

set. In this manner
the

NavigationFilter

can effectively restrict where the
cursor can be positioned. Similarly

DefaultCaret

will call
into the

NavigationFilter

when the user is changing the
selection to further restrict where the cursor can be positioned.

Subclasses can conditionally call into supers implementation to restrict
where the cursor can be placed, or call directly into the

FilterBypass

.

**Since:** 1.4
**See Also:** Caret

,

DefaultCaret

,

View

---

### Field Details

*No entries found.*

### Constructor Details

#### public NavigationFilter()

*No description found.*

---

### Method Details

#### public void setDot​(
NavigationFilter.FilterBypass
fb,
int dot,

Position.Bias
bias)

Invoked prior to the Caret setting the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary method
on the

FilterBypass

**Parameters:**
- fb

- FilterBypass that can be used to mutate caret position
- dot

- the position >= 0
- bias

- Bias to place the dot at

---

#### public void moveDot​(
NavigationFilter.FilterBypass
fb,
int dot,

Position.Bias
bias)

Invoked prior to the Caret moving the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary
methods on the

FilterBypass

.

**Parameters:**
- fb

- FilterBypass that can be used to mutate caret position
- dot

- the position >= 0
- bias

- Bias for new location

---

#### public int getNextVisualPositionFrom​(
JTextComponent
text,
int pos,

Position.Bias
bias,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException

Returns the next visual position to place the caret at from an
existing position. The default implementation simply forwards the
method to the root View. Subclasses may wish to further restrict the
location based on additional criteria.

**Parameters:**
- text

- JTextComponent containing text
- pos

- Position used in determining next position
- bias

- Bias used in determining next position
- direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This will be one of the following values:

- SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH
- biasRet

- Used to return resulting Bias of next position

**Returns:**
- the location within the model that best represents the next
location visual position

**Throws:**
- BadLocationException

- for a bad location within a document model
- IllegalArgumentException

- if

direction

doesn't have one of the legal values above

---

### Additional Sections

#### Class NavigationFilter

java.lang.Object

- javax.swing.text.NavigationFilter

javax.swing.text.NavigationFilter

```java
public class
NavigationFilter

extends
Object
```

NavigationFilter

can be used to restrict where the cursor can
be positioned. When the default cursor positioning actions attempt to
reposition the cursor they will call into the

NavigationFilter

, assuming
the

JTextComponent

has a non-null

NavigationFilter

set. In this manner
the

NavigationFilter

can effectively restrict where the
cursor can be positioned. Similarly

DefaultCaret

will call
into the

NavigationFilter

when the user is changing the
selection to further restrict where the cursor can be positioned.

Subclasses can conditionally call into supers implementation to restrict
where the cursor can be placed, or call directly into the

FilterBypass

.

**Since:** 1.4
**See Also:** Caret

,

DefaultCaret

,

View

public class

NavigationFilter

extends

Object

NavigationFilter

can be used to restrict where the cursor can
be positioned. When the default cursor positioning actions attempt to
reposition the cursor they will call into the

NavigationFilter

, assuming
the

JTextComponent

has a non-null

NavigationFilter

set. In this manner
the

NavigationFilter

can effectively restrict where the
cursor can be positioned. Similarly

DefaultCaret

will call
into the

NavigationFilter

when the user is changing the
selection to further restrict where the cursor can be positioned.

Subclasses can conditionally call into supers implementation to restrict
where the cursor can be placed, or call directly into the

FilterBypass

.

Subclasses can conditionally call into supers implementation to restrict
where the cursor can be placed, or call directly into the

FilterBypass

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

NavigationFilter.FilterBypass

Used as a way to circumvent calling back into the caret to
position the cursor.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NavigationFilter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getNextVisualPositionFrom

​(

JTextComponent

text,
int pos,

Position.Bias

bias,
int direction,

Position.Bias

[] biasRet)

Returns the next visual position to place the caret at from an
existing position.

void

moveDot

​(

NavigationFilter.FilterBypass

fb,
int dot,

Position.Bias

bias)

Invoked prior to the Caret moving the dot.

void

setDot

​(

NavigationFilter.FilterBypass

fb,
int dot,

Position.Bias

bias)

Invoked prior to the Caret setting the dot.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

NavigationFilter.FilterBypass

Used as a way to circumvent calling back into the caret to
position the cursor.

---

#### Nested Class Summary

Used as a way to circumvent calling back into the caret to
position the cursor.

Constructor Summary

Constructors

Constructor

Description

NavigationFilter

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

int

getNextVisualPositionFrom

​(

JTextComponent

text,
int pos,

Position.Bias

bias,
int direction,

Position.Bias

[] biasRet)

Returns the next visual position to place the caret at from an
existing position.

void

moveDot

​(

NavigationFilter.FilterBypass

fb,
int dot,

Position.Bias

bias)

Invoked prior to the Caret moving the dot.

void

setDot

​(

NavigationFilter.FilterBypass

fb,
int dot,

Position.Bias

bias)

Invoked prior to the Caret setting the dot.

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

Returns the next visual position to place the caret at from an
existing position.

Invoked prior to the Caret moving the dot.

Invoked prior to the Caret setting the dot.

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

- NavigationFilter

```java
public NavigationFilter()
```

============ METHOD DETAIL ==========

- Method Detail

- setDot

```java
public void setDot​(
NavigationFilter.FilterBypass
fb,
int dot,

Position.Bias
bias)
```

Invoked prior to the Caret setting the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary method
on the

FilterBypass

**Parameters:** fb

- FilterBypass that can be used to mutate caret position
**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias to place the dot at

- moveDot

```java
public void moveDot​(
NavigationFilter.FilterBypass
fb,
int dot,

Position.Bias
bias)
```

Invoked prior to the Caret moving the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary
methods on the

FilterBypass

.

**Parameters:** fb

- FilterBypass that can be used to mutate caret position
**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias for new location

- getNextVisualPositionFrom

```java
public int getNextVisualPositionFrom​(
JTextComponent
text,
int pos,

Position.Bias
bias,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Returns the next visual position to place the caret at from an
existing position. The default implementation simply forwards the
method to the root View. Subclasses may wish to further restrict the
location based on additional criteria.

**Parameters:** text

- JTextComponent containing text
**Parameters:** pos

- Position used in determining next position
**Parameters:** bias

- Bias used in determining next position
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This will be one of the following values:

- SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH
**Parameters:** biasRet

- Used to return resulting Bias of next position
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- if

direction

doesn't have one of the legal values above

Constructor Detail

- NavigationFilter

```java
public NavigationFilter()
```

---

#### Constructor Detail

NavigationFilter

```java
public NavigationFilter()
```

---

#### NavigationFilter

public NavigationFilter()

Method Detail

- setDot

```java
public void setDot​(
NavigationFilter.FilterBypass
fb,
int dot,

Position.Bias
bias)
```

Invoked prior to the Caret setting the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary method
on the

FilterBypass

**Parameters:** fb

- FilterBypass that can be used to mutate caret position
**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias to place the dot at

- moveDot

```java
public void moveDot​(
NavigationFilter.FilterBypass
fb,
int dot,

Position.Bias
bias)
```

Invoked prior to the Caret moving the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary
methods on the

FilterBypass

.

**Parameters:** fb

- FilterBypass that can be used to mutate caret position
**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias for new location

- getNextVisualPositionFrom

```java
public int getNextVisualPositionFrom​(
JTextComponent
text,
int pos,

Position.Bias
bias,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Returns the next visual position to place the caret at from an
existing position. The default implementation simply forwards the
method to the root View. Subclasses may wish to further restrict the
location based on additional criteria.

**Parameters:** text

- JTextComponent containing text
**Parameters:** pos

- Position used in determining next position
**Parameters:** bias

- Bias used in determining next position
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This will be one of the following values:

- SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH
**Parameters:** biasRet

- Used to return resulting Bias of next position
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- if

direction

doesn't have one of the legal values above

---

#### Method Detail

setDot

```java
public void setDot​(
NavigationFilter.FilterBypass
fb,
int dot,

Position.Bias
bias)
```

Invoked prior to the Caret setting the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary method
on the

FilterBypass

**Parameters:** fb

- FilterBypass that can be used to mutate caret position
**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias to place the dot at

---

#### setDot

public void setDot​(

NavigationFilter.FilterBypass

fb,
int dot,

Position.Bias

bias)

Invoked prior to the Caret setting the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary method
on the

FilterBypass

moveDot

```java
public void moveDot​(
NavigationFilter.FilterBypass
fb,
int dot,

Position.Bias
bias)
```

Invoked prior to the Caret moving the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary
methods on the

FilterBypass

.

**Parameters:** fb

- FilterBypass that can be used to mutate caret position
**Parameters:** dot

- the position >= 0
**Parameters:** bias

- Bias for new location

---

#### moveDot

public void moveDot​(

NavigationFilter.FilterBypass

fb,
int dot,

Position.Bias

bias)

Invoked prior to the Caret moving the dot. The default implementation
calls directly into the

FilterBypass

with the passed
in arguments. Subclasses may wish to conditionally
call super with a different location, or invoke the necessary
methods on the

FilterBypass

.

getNextVisualPositionFrom

```java
public int getNextVisualPositionFrom​(
JTextComponent
text,
int pos,

Position.Bias
bias,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Returns the next visual position to place the caret at from an
existing position. The default implementation simply forwards the
method to the root View. Subclasses may wish to further restrict the
location based on additional criteria.

**Parameters:** text

- JTextComponent containing text
**Parameters:** pos

- Position used in determining next position
**Parameters:** bias

- Bias used in determining next position
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This will be one of the following values:

- SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH
**Parameters:** biasRet

- Used to return resulting Bias of next position
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- if

direction

doesn't have one of the legal values above

---

#### getNextVisualPositionFrom

public int getNextVisualPositionFrom​(

JTextComponent

text,
int pos,

Position.Bias

bias,
int direction,

Position.Bias

[] biasRet)
throws

BadLocationException

Returns the next visual position to place the caret at from an
existing position. The default implementation simply forwards the
method to the root View. Subclasses may wish to further restrict the
location based on additional criteria.

SwingConstants.WEST

SwingConstants.EAST

SwingConstants.NORTH

SwingConstants.SOUTH

---

