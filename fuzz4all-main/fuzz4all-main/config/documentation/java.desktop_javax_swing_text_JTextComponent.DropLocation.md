# Class JTextComponent.DropLocation

**Source:** `java.desktop\javax\swing\text\JTextComponent.DropLocation.html`

### Class Description

```java
public static final class
JTextComponent.DropLocation

extends
TransferHandler.DropLocation
```

Represents a drop location for

JTextComponent

s.

**Enclosing class:** JTextComponent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public int getIndex()

Returns the index where dropped data should be inserted into the
associated component. This index represents a position between
characters, as would be interpreted by a caret.

**Returns:**
- the drop index

---

#### public
Position.Bias
getBias()

Returns the bias for the drop index.

**Returns:**
- the drop bias

---

#### public
String
toString()

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:**
- toString

in class

TransferHandler.DropLocation

**Returns:**
- a string representation of this drop location

---

### Additional Sections

#### Class JTextComponent.DropLocation

java.lang.Object

- javax.swing.TransferHandler.DropLocation
- - javax.swing.text.JTextComponent.DropLocation

javax.swing.TransferHandler.DropLocation

- javax.swing.text.JTextComponent.DropLocation

javax.swing.text.JTextComponent.DropLocation

**Enclosing class:** JTextComponent

```java
public static final class
JTextComponent.DropLocation

extends
TransferHandler.DropLocation
```

Represents a drop location for

JTextComponent

s.

**Since:** 1.6
**See Also:** JTextComponent.getDropLocation()

public static final class

JTextComponent.DropLocation

extends

TransferHandler.DropLocation

Represents a drop location for

JTextComponent

s.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Position.Bias

getBias

()

Returns the bias for the drop index.

int

getIndex

()

Returns the index where dropped data should be inserted into the
associated component.

String

toString

()

Returns a string representation of this drop location.

- Methods declared in class javax.swing.

TransferHandler.DropLocation

getDropPoint

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Position.Bias

getBias

()

Returns the bias for the drop index.

int

getIndex

()

Returns the index where dropped data should be inserted into the
associated component.

String

toString

()

Returns a string representation of this drop location.

- Methods declared in class javax.swing.

TransferHandler.DropLocation

getDropPoint

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

Returns the bias for the drop index.

Returns the index where dropped data should be inserted into the
associated component.

Returns a string representation of this drop location.

Methods declared in class javax.swing.

TransferHandler.DropLocation

getDropPoint

---

#### Methods declared in class javax.swing. TransferHandler.DropLocation

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

============ METHOD DETAIL ==========

- Method Detail

- getIndex

```java
public int getIndex()
```

Returns the index where dropped data should be inserted into the
associated component. This index represents a position between
characters, as would be interpreted by a caret.

**Returns:** the drop index

- getBias

```java
public
Position.Bias
getBias()
```

Returns the bias for the drop index.

**Returns:** the drop bias

- toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

TransferHandler.DropLocation
**Returns:** a string representation of this drop location

Method Detail

- getIndex

```java
public int getIndex()
```

Returns the index where dropped data should be inserted into the
associated component. This index represents a position between
characters, as would be interpreted by a caret.

**Returns:** the drop index

- getBias

```java
public
Position.Bias
getBias()
```

Returns the bias for the drop index.

**Returns:** the drop bias

- toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

TransferHandler.DropLocation
**Returns:** a string representation of this drop location

---

#### Method Detail

getIndex

```java
public int getIndex()
```

Returns the index where dropped data should be inserted into the
associated component. This index represents a position between
characters, as would be interpreted by a caret.

**Returns:** the drop index

---

#### getIndex

public int getIndex()

Returns the index where dropped data should be inserted into the
associated component. This index represents a position between
characters, as would be interpreted by a caret.

getBias

```java
public
Position.Bias
getBias()
```

Returns the bias for the drop index.

**Returns:** the drop bias

---

#### getBias

public

Position.Bias

getBias()

Returns the bias for the drop index.

toString

```java
public
String
toString()
```

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

**Overrides:** toString

in class

TransferHandler.DropLocation
**Returns:** a string representation of this drop location

---

#### toString

public

String

toString()

Returns a string representation of this drop location.
This method is intended to be used for debugging purposes,
and the content and format of the returned string may vary
between implementations.

---

