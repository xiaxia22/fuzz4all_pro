# Class JFormattedTextField.AbstractFormatterFactory

**Source:** `java.desktop\javax\swing\JFormattedTextField.AbstractFormatterFactory.html`

### Class Description

```java
public abstract static class
JFormattedTextField.AbstractFormatterFactory

extends
Object
```

Instances of

AbstractFormatterFactory

are used by

JFormattedTextField

to obtain instances of

AbstractFormatter

which in turn are used to format values.

AbstractFormatterFactory

can return different

AbstractFormatter

s based on the state of the

JFormattedTextField

, perhaps returning different

AbstractFormatter

s when the

JFormattedTextField

has focus vs when it
doesn't have focus.

**Direct Known Subclasses:** DefaultFormatterFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### public AbstractFormatterFactory()

*No description found.*

---

### Method Details

#### public abstract
JFormattedTextField.AbstractFormatter
getFormatter​(
JFormattedTextField
tf)

Returns an

AbstractFormatter

that can handle formatting
of the passed in

JFormattedTextField

.

**Parameters:**
- tf

- JFormattedTextField requesting AbstractFormatter

**Returns:**
- AbstractFormatter to handle formatting duties, a null
return value implies the JFormattedTextField should behave
like a normal JTextField

---

### Additional Sections

#### Class JFormattedTextField.AbstractFormatterFactory

java.lang.Object

- javax.swing.JFormattedTextField.AbstractFormatterFactory

javax.swing.JFormattedTextField.AbstractFormatterFactory

**Direct Known Subclasses:** DefaultFormatterFactory

**Enclosing class:** JFormattedTextField

```java
public abstract static class
JFormattedTextField.AbstractFormatterFactory

extends
Object
```

Instances of

AbstractFormatterFactory

are used by

JFormattedTextField

to obtain instances of

AbstractFormatter

which in turn are used to format values.

AbstractFormatterFactory

can return different

AbstractFormatter

s based on the state of the

JFormattedTextField

, perhaps returning different

AbstractFormatter

s when the

JFormattedTextField

has focus vs when it
doesn't have focus.

**Since:** 1.4

public abstract static class

JFormattedTextField.AbstractFormatterFactory

extends

Object

Instances of

AbstractFormatterFactory

are used by

JFormattedTextField

to obtain instances of

AbstractFormatter

which in turn are used to format values.

AbstractFormatterFactory

can return different

AbstractFormatter

s based on the state of the

JFormattedTextField

, perhaps returning different

AbstractFormatter

s when the

JFormattedTextField

has focus vs when it
doesn't have focus.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractFormatterFactory

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

JFormattedTextField.AbstractFormatter

getFormatter

​(

JFormattedTextField

tf)

Returns an

AbstractFormatter

that can handle formatting
of the passed in

JFormattedTextField

.

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

AbstractFormatterFactory

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

JFormattedTextField.AbstractFormatter

getFormatter

​(

JFormattedTextField

tf)

Returns an

AbstractFormatter

that can handle formatting
of the passed in

JFormattedTextField

.

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

Returns an

AbstractFormatter

that can handle formatting
of the passed in

JFormattedTextField

.

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

- AbstractFormatterFactory

```java
public AbstractFormatterFactory()
```

============ METHOD DETAIL ==========

- Method Detail

- getFormatter

```java
public abstract
JFormattedTextField.AbstractFormatter
getFormatter​(
JFormattedTextField
tf)
```

Returns an

AbstractFormatter

that can handle formatting
of the passed in

JFormattedTextField

.

**Parameters:** tf

- JFormattedTextField requesting AbstractFormatter
**Returns:** AbstractFormatter to handle formatting duties, a null
return value implies the JFormattedTextField should behave
like a normal JTextField

Constructor Detail

- AbstractFormatterFactory

```java
public AbstractFormatterFactory()
```

---

#### Constructor Detail

AbstractFormatterFactory

```java
public AbstractFormatterFactory()
```

---

#### AbstractFormatterFactory

public AbstractFormatterFactory()

Method Detail

- getFormatter

```java
public abstract
JFormattedTextField.AbstractFormatter
getFormatter​(
JFormattedTextField
tf)
```

Returns an

AbstractFormatter

that can handle formatting
of the passed in

JFormattedTextField

.

**Parameters:** tf

- JFormattedTextField requesting AbstractFormatter
**Returns:** AbstractFormatter to handle formatting duties, a null
return value implies the JFormattedTextField should behave
like a normal JTextField

---

#### Method Detail

getFormatter

```java
public abstract
JFormattedTextField.AbstractFormatter
getFormatter​(
JFormattedTextField
tf)
```

Returns an

AbstractFormatter

that can handle formatting
of the passed in

JFormattedTextField

.

**Parameters:** tf

- JFormattedTextField requesting AbstractFormatter
**Returns:** AbstractFormatter to handle formatting duties, a null
return value implies the JFormattedTextField should behave
like a normal JTextField

---

#### getFormatter

public abstract

JFormattedTextField.AbstractFormatter

getFormatter​(

JFormattedTextField

tf)

Returns an

AbstractFormatter

that can handle formatting
of the passed in

JFormattedTextField

.

---

