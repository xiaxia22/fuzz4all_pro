# Interface Adjustable

**Source:** `java.desktop\java\awt\Adjustable.html`

### Class Description

```java
public interface
Adjustable
```

The interface for objects which have an adjustable numeric value
contained within a bounded range of values.

**All Known Implementing Classes:** JScrollBar

,

JScrollPane.ScrollBar

,

Scrollbar

,

ScrollPaneAdjustable

---

### Field Details

#### @Native

static final int HORIZONTAL

Indicates that the

Adjustable

has horizontal orientation.

**See Also:**
- Constant Field Values

---

#### @Native

static final int VERTICAL

Indicates that the

Adjustable

has vertical orientation.

**See Also:**
- Constant Field Values

---

#### @Native

static final int NO_ORIENTATION

Indicates that the

Adjustable

has no orientation.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getOrientation()

Gets the orientation of the adjustable object.

**Returns:**
- the orientation of the adjustable object;
either

HORIZONTAL

,

VERTICAL

,
or

NO_ORIENTATION

---

#### void setMinimum​(int min)

Sets the minimum value of the adjustable object.

**Parameters:**
- min

- the minimum value

---

#### int getMinimum()

Gets the minimum value of the adjustable object.

**Returns:**
- the minimum value of the adjustable object

---

#### void setMaximum​(int max)

Sets the maximum value of the adjustable object.

**Parameters:**
- max

- the maximum value

---

#### int getMaximum()

Gets the maximum value of the adjustable object.

**Returns:**
- the maximum value of the adjustable object

---

#### void setUnitIncrement​(int u)

Sets the unit value increment for the adjustable object.

**Parameters:**
- u

- the unit increment

---

#### int getUnitIncrement()

Gets the unit value increment for the adjustable object.

**Returns:**
- the unit value increment for the adjustable object

---

#### void setBlockIncrement​(int b)

Sets the block value increment for the adjustable object.

**Parameters:**
- b

- the block increment

---

#### int getBlockIncrement()

Gets the block value increment for the adjustable object.

**Returns:**
- the block value increment for the adjustable object

---

#### void setVisibleAmount​(int v)

Sets the length of the proportional indicator of the
adjustable object.

**Parameters:**
- v

- the length of the indicator

---

#### int getVisibleAmount()

Gets the length of the proportional indicator.

**Returns:**
- the length of the proportional indicator

---

#### void setValue​(int v)

Sets the current value of the adjustable object. If
the value supplied is less than

minimum

or greater than

maximum

-

visibleAmount

,
then one of those values is substituted, as appropriate.

Calling this method does not fire an

AdjustmentEvent

.

**Parameters:**
- v

- the current value, between

minimum

and

maximum

-

visibleAmount

---

#### int getValue()

Gets the current value of the adjustable object.

**Returns:**
- the current value of the adjustable object

---

#### void addAdjustmentListener​(
AdjustmentListener
l)

Adds a listener to receive adjustment events when the value of
the adjustable object changes.

**Parameters:**
- l

- the listener to receive events

**See Also:**
- AdjustmentEvent

---

#### void removeAdjustmentListener​(
AdjustmentListener
l)

Removes an adjustment listener.

**Parameters:**
- l

- the listener being removed

**See Also:**
- AdjustmentEvent

---

### Additional Sections

#### Interface Adjustable

**All Known Implementing Classes:** JScrollBar

,

JScrollPane.ScrollBar

,

Scrollbar

,

ScrollPaneAdjustable

```java
public interface
Adjustable
```

The interface for objects which have an adjustable numeric value
contained within a bounded range of values.

public interface

Adjustable

The interface for objects which have an adjustable numeric value
contained within a bounded range of values.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

HORIZONTAL

Indicates that the

Adjustable

has horizontal orientation.

static int

NO_ORIENTATION

Indicates that the

Adjustable

has no orientation.

static int

VERTICAL

Indicates that the

Adjustable

has vertical orientation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addAdjustmentListener

​(

AdjustmentListener

l)

Adds a listener to receive adjustment events when the value of
the adjustable object changes.

int

getBlockIncrement

()

Gets the block value increment for the adjustable object.

int

getMaximum

()

Gets the maximum value of the adjustable object.

int

getMinimum

()

Gets the minimum value of the adjustable object.

int

getOrientation

()

Gets the orientation of the adjustable object.

int

getUnitIncrement

()

Gets the unit value increment for the adjustable object.

int

getValue

()

Gets the current value of the adjustable object.

int

getVisibleAmount

()

Gets the length of the proportional indicator.

void

removeAdjustmentListener

​(

AdjustmentListener

l)

Removes an adjustment listener.

void

setBlockIncrement

​(int b)

Sets the block value increment for the adjustable object.

void

setMaximum

​(int max)

Sets the maximum value of the adjustable object.

void

setMinimum

​(int min)

Sets the minimum value of the adjustable object.

void

setUnitIncrement

​(int u)

Sets the unit value increment for the adjustable object.

void

setValue

​(int v)

Sets the current value of the adjustable object.

void

setVisibleAmount

​(int v)

Sets the length of the proportional indicator of the
adjustable object.

Field Summary

Fields

Modifier and Type

Field

Description

static int

HORIZONTAL

Indicates that the

Adjustable

has horizontal orientation.

static int

NO_ORIENTATION

Indicates that the

Adjustable

has no orientation.

static int

VERTICAL

Indicates that the

Adjustable

has vertical orientation.

---

#### Field Summary

Indicates that the

Adjustable

has horizontal orientation.

Indicates that the

Adjustable

has no orientation.

Indicates that the

Adjustable

has vertical orientation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addAdjustmentListener

​(

AdjustmentListener

l)

Adds a listener to receive adjustment events when the value of
the adjustable object changes.

int

getBlockIncrement

()

Gets the block value increment for the adjustable object.

int

getMaximum

()

Gets the maximum value of the adjustable object.

int

getMinimum

()

Gets the minimum value of the adjustable object.

int

getOrientation

()

Gets the orientation of the adjustable object.

int

getUnitIncrement

()

Gets the unit value increment for the adjustable object.

int

getValue

()

Gets the current value of the adjustable object.

int

getVisibleAmount

()

Gets the length of the proportional indicator.

void

removeAdjustmentListener

​(

AdjustmentListener

l)

Removes an adjustment listener.

void

setBlockIncrement

​(int b)

Sets the block value increment for the adjustable object.

void

setMaximum

​(int max)

Sets the maximum value of the adjustable object.

void

setMinimum

​(int min)

Sets the minimum value of the adjustable object.

void

setUnitIncrement

​(int u)

Sets the unit value increment for the adjustable object.

void

setValue

​(int v)

Sets the current value of the adjustable object.

void

setVisibleAmount

​(int v)

Sets the length of the proportional indicator of the
adjustable object.

---

#### Method Summary

Adds a listener to receive adjustment events when the value of
the adjustable object changes.

Gets the block value increment for the adjustable object.

Gets the maximum value of the adjustable object.

Gets the minimum value of the adjustable object.

Gets the orientation of the adjustable object.

Gets the unit value increment for the adjustable object.

Gets the current value of the adjustable object.

Gets the length of the proportional indicator.

Removes an adjustment listener.

Sets the block value increment for the adjustable object.

Sets the maximum value of the adjustable object.

Sets the minimum value of the adjustable object.

Sets the unit value increment for the adjustable object.

Sets the current value of the adjustable object.

Sets the length of the proportional indicator of the
adjustable object.

============ FIELD DETAIL ===========

- Field Detail

- HORIZONTAL

```java
@Native

static final int HORIZONTAL
```

Indicates that the

Adjustable

has horizontal orientation.

**See Also:** Constant Field Values

- VERTICAL

```java
@Native

static final int VERTICAL
```

Indicates that the

Adjustable

has vertical orientation.

**See Also:** Constant Field Values

- NO_ORIENTATION

```java
@Native

static final int NO_ORIENTATION
```

Indicates that the

Adjustable

has no orientation.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getOrientation

```java
int getOrientation()
```

Gets the orientation of the adjustable object.

**Returns:** the orientation of the adjustable object;
either

HORIZONTAL

,

VERTICAL

,
or

NO_ORIENTATION

- setMinimum

```java
void setMinimum​(int min)
```

Sets the minimum value of the adjustable object.

**Parameters:** min

- the minimum value

- getMinimum

```java
int getMinimum()
```

Gets the minimum value of the adjustable object.

**Returns:** the minimum value of the adjustable object

- setMaximum

```java
void setMaximum​(int max)
```

Sets the maximum value of the adjustable object.

**Parameters:** max

- the maximum value

- getMaximum

```java
int getMaximum()
```

Gets the maximum value of the adjustable object.

**Returns:** the maximum value of the adjustable object

- setUnitIncrement

```java
void setUnitIncrement​(int u)
```

Sets the unit value increment for the adjustable object.

**Parameters:** u

- the unit increment

- getUnitIncrement

```java
int getUnitIncrement()
```

Gets the unit value increment for the adjustable object.

**Returns:** the unit value increment for the adjustable object

- setBlockIncrement

```java
void setBlockIncrement​(int b)
```

Sets the block value increment for the adjustable object.

**Parameters:** b

- the block increment

- getBlockIncrement

```java
int getBlockIncrement()
```

Gets the block value increment for the adjustable object.

**Returns:** the block value increment for the adjustable object

- setVisibleAmount

```java
void setVisibleAmount​(int v)
```

Sets the length of the proportional indicator of the
adjustable object.

**Parameters:** v

- the length of the indicator

- getVisibleAmount

```java
int getVisibleAmount()
```

Gets the length of the proportional indicator.

**Returns:** the length of the proportional indicator

- setValue

```java
void setValue​(int v)
```

Sets the current value of the adjustable object. If
the value supplied is less than

minimum

or greater than

maximum

-

visibleAmount

,
then one of those values is substituted, as appropriate.

Calling this method does not fire an

AdjustmentEvent

.

**Parameters:** v

- the current value, between

minimum

and

maximum

-

visibleAmount

- getValue

```java
int getValue()
```

Gets the current value of the adjustable object.

**Returns:** the current value of the adjustable object

- addAdjustmentListener

```java
void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds a listener to receive adjustment events when the value of
the adjustable object changes.

**Parameters:** l

- the listener to receive events
**See Also:** AdjustmentEvent

- removeAdjustmentListener

```java
void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes an adjustment listener.

**Parameters:** l

- the listener being removed
**See Also:** AdjustmentEvent

Field Detail

- HORIZONTAL

```java
@Native

static final int HORIZONTAL
```

Indicates that the

Adjustable

has horizontal orientation.

**See Also:** Constant Field Values

- VERTICAL

```java
@Native

static final int VERTICAL
```

Indicates that the

Adjustable

has vertical orientation.

**See Also:** Constant Field Values

- NO_ORIENTATION

```java
@Native

static final int NO_ORIENTATION
```

Indicates that the

Adjustable

has no orientation.

**See Also:** Constant Field Values

---

#### Field Detail

HORIZONTAL

```java
@Native

static final int HORIZONTAL
```

Indicates that the

Adjustable

has horizontal orientation.

**See Also:** Constant Field Values

---

#### HORIZONTAL

@Native

static final int HORIZONTAL

Indicates that the

Adjustable

has horizontal orientation.

VERTICAL

```java
@Native

static final int VERTICAL
```

Indicates that the

Adjustable

has vertical orientation.

**See Also:** Constant Field Values

---

#### VERTICAL

@Native

static final int VERTICAL

Indicates that the

Adjustable

has vertical orientation.

NO_ORIENTATION

```java
@Native

static final int NO_ORIENTATION
```

Indicates that the

Adjustable

has no orientation.

**See Also:** Constant Field Values

---

#### NO_ORIENTATION

@Native

static final int NO_ORIENTATION

Indicates that the

Adjustable

has no orientation.

Method Detail

- getOrientation

```java
int getOrientation()
```

Gets the orientation of the adjustable object.

**Returns:** the orientation of the adjustable object;
either

HORIZONTAL

,

VERTICAL

,
or

NO_ORIENTATION

- setMinimum

```java
void setMinimum​(int min)
```

Sets the minimum value of the adjustable object.

**Parameters:** min

- the minimum value

- getMinimum

```java
int getMinimum()
```

Gets the minimum value of the adjustable object.

**Returns:** the minimum value of the adjustable object

- setMaximum

```java
void setMaximum​(int max)
```

Sets the maximum value of the adjustable object.

**Parameters:** max

- the maximum value

- getMaximum

```java
int getMaximum()
```

Gets the maximum value of the adjustable object.

**Returns:** the maximum value of the adjustable object

- setUnitIncrement

```java
void setUnitIncrement​(int u)
```

Sets the unit value increment for the adjustable object.

**Parameters:** u

- the unit increment

- getUnitIncrement

```java
int getUnitIncrement()
```

Gets the unit value increment for the adjustable object.

**Returns:** the unit value increment for the adjustable object

- setBlockIncrement

```java
void setBlockIncrement​(int b)
```

Sets the block value increment for the adjustable object.

**Parameters:** b

- the block increment

- getBlockIncrement

```java
int getBlockIncrement()
```

Gets the block value increment for the adjustable object.

**Returns:** the block value increment for the adjustable object

- setVisibleAmount

```java
void setVisibleAmount​(int v)
```

Sets the length of the proportional indicator of the
adjustable object.

**Parameters:** v

- the length of the indicator

- getVisibleAmount

```java
int getVisibleAmount()
```

Gets the length of the proportional indicator.

**Returns:** the length of the proportional indicator

- setValue

```java
void setValue​(int v)
```

Sets the current value of the adjustable object. If
the value supplied is less than

minimum

or greater than

maximum

-

visibleAmount

,
then one of those values is substituted, as appropriate.

Calling this method does not fire an

AdjustmentEvent

.

**Parameters:** v

- the current value, between

minimum

and

maximum

-

visibleAmount

- getValue

```java
int getValue()
```

Gets the current value of the adjustable object.

**Returns:** the current value of the adjustable object

- addAdjustmentListener

```java
void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds a listener to receive adjustment events when the value of
the adjustable object changes.

**Parameters:** l

- the listener to receive events
**See Also:** AdjustmentEvent

- removeAdjustmentListener

```java
void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes an adjustment listener.

**Parameters:** l

- the listener being removed
**See Also:** AdjustmentEvent

---

#### Method Detail

getOrientation

```java
int getOrientation()
```

Gets the orientation of the adjustable object.

**Returns:** the orientation of the adjustable object;
either

HORIZONTAL

,

VERTICAL

,
or

NO_ORIENTATION

---

#### getOrientation

int getOrientation()

Gets the orientation of the adjustable object.

setMinimum

```java
void setMinimum​(int min)
```

Sets the minimum value of the adjustable object.

**Parameters:** min

- the minimum value

---

#### setMinimum

void setMinimum​(int min)

Sets the minimum value of the adjustable object.

getMinimum

```java
int getMinimum()
```

Gets the minimum value of the adjustable object.

**Returns:** the minimum value of the adjustable object

---

#### getMinimum

int getMinimum()

Gets the minimum value of the adjustable object.

setMaximum

```java
void setMaximum​(int max)
```

Sets the maximum value of the adjustable object.

**Parameters:** max

- the maximum value

---

#### setMaximum

void setMaximum​(int max)

Sets the maximum value of the adjustable object.

getMaximum

```java
int getMaximum()
```

Gets the maximum value of the adjustable object.

**Returns:** the maximum value of the adjustable object

---

#### getMaximum

int getMaximum()

Gets the maximum value of the adjustable object.

setUnitIncrement

```java
void setUnitIncrement​(int u)
```

Sets the unit value increment for the adjustable object.

**Parameters:** u

- the unit increment

---

#### setUnitIncrement

void setUnitIncrement​(int u)

Sets the unit value increment for the adjustable object.

getUnitIncrement

```java
int getUnitIncrement()
```

Gets the unit value increment for the adjustable object.

**Returns:** the unit value increment for the adjustable object

---

#### getUnitIncrement

int getUnitIncrement()

Gets the unit value increment for the adjustable object.

setBlockIncrement

```java
void setBlockIncrement​(int b)
```

Sets the block value increment for the adjustable object.

**Parameters:** b

- the block increment

---

#### setBlockIncrement

void setBlockIncrement​(int b)

Sets the block value increment for the adjustable object.

getBlockIncrement

```java
int getBlockIncrement()
```

Gets the block value increment for the adjustable object.

**Returns:** the block value increment for the adjustable object

---

#### getBlockIncrement

int getBlockIncrement()

Gets the block value increment for the adjustable object.

setVisibleAmount

```java
void setVisibleAmount​(int v)
```

Sets the length of the proportional indicator of the
adjustable object.

**Parameters:** v

- the length of the indicator

---

#### setVisibleAmount

void setVisibleAmount​(int v)

Sets the length of the proportional indicator of the
adjustable object.

getVisibleAmount

```java
int getVisibleAmount()
```

Gets the length of the proportional indicator.

**Returns:** the length of the proportional indicator

---

#### getVisibleAmount

int getVisibleAmount()

Gets the length of the proportional indicator.

setValue

```java
void setValue​(int v)
```

Sets the current value of the adjustable object. If
the value supplied is less than

minimum

or greater than

maximum

-

visibleAmount

,
then one of those values is substituted, as appropriate.

Calling this method does not fire an

AdjustmentEvent

.

**Parameters:** v

- the current value, between

minimum

and

maximum

-

visibleAmount

---

#### setValue

void setValue​(int v)

Sets the current value of the adjustable object. If
the value supplied is less than

minimum

or greater than

maximum

-

visibleAmount

,
then one of those values is substituted, as appropriate.

Calling this method does not fire an

AdjustmentEvent

.

Calling this method does not fire an

AdjustmentEvent

.

getValue

```java
int getValue()
```

Gets the current value of the adjustable object.

**Returns:** the current value of the adjustable object

---

#### getValue

int getValue()

Gets the current value of the adjustable object.

addAdjustmentListener

```java
void addAdjustmentListener​(
AdjustmentListener
l)
```

Adds a listener to receive adjustment events when the value of
the adjustable object changes.

**Parameters:** l

- the listener to receive events
**See Also:** AdjustmentEvent

---

#### addAdjustmentListener

void addAdjustmentListener​(

AdjustmentListener

l)

Adds a listener to receive adjustment events when the value of
the adjustable object changes.

removeAdjustmentListener

```java
void removeAdjustmentListener​(
AdjustmentListener
l)
```

Removes an adjustment listener.

**Parameters:** l

- the listener being removed
**See Also:** AdjustmentEvent

---

#### removeAdjustmentListener

void removeAdjustmentListener​(

AdjustmentListener

l)

Removes an adjustment listener.

---

