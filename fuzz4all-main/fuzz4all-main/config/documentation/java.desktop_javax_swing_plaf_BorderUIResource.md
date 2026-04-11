# Class BorderUIResource

**Source:** `java.desktop\javax\swing\plaf\BorderUIResource.html`

### Class Description

```java
public class
BorderUIResource

extends
Object

implements
Border
,
UIResource
,
Serializable
```

A Border wrapper class which implements UIResource. UI
classes which set border properties should use this class
to wrap any borders specified as defaults.

This class delegates all method invocations to the
Border "delegate" object specified at construction.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

Border

,

UIResource

---

### Field Details

*No entries found.*

### Constructor Details

#### public BorderUIResource​(
Border
delegate)

Creates a UIResource border object which wraps
an existing Border instance.

**Parameters:**
- delegate

- the border being wrapped

---

### Method Details

#### public static
Border
getEtchedBorderUIResource()

Returns a etched border UI resource.

**Returns:**
- a etched border UI resource

---

#### public static
Border
getLoweredBevelBorderUIResource()

Returns a lowered bevel border UI resource.

**Returns:**
- a lowered bevel border UI resource

---

#### public static
Border
getRaisedBevelBorderUIResource()

Returns a raised bevel border UI resource.

**Returns:**
- a raised bevel border UI resource

---

#### public static
Border
getBlackLineBorderUIResource()

Returns a black line border UI resource.

**Returns:**
- a black line border UI resource

---

### Additional Sections

#### Class BorderUIResource

java.lang.Object

- javax.swing.plaf.BorderUIResource

javax.swing.plaf.BorderUIResource

**All Implemented Interfaces:** Serializable

,

Border

,

UIResource

```java
public class
BorderUIResource

extends
Object

implements
Border
,
UIResource
,
Serializable
```

A Border wrapper class which implements UIResource. UI
classes which set border properties should use this class
to wrap any borders specified as defaults.

This class delegates all method invocations to the
Border "delegate" object specified at construction.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** UIResource

,

Serialized Form

public class

BorderUIResource

extends

Object

implements

Border

,

UIResource

,

Serializable

A Border wrapper class which implements UIResource. UI
classes which set border properties should use this class
to wrap any borders specified as defaults.

This class delegates all method invocations to the
Border "delegate" object specified at construction.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

BorderUIResource.BevelBorderUIResource

A bevel border UI resource.

static class

BorderUIResource.CompoundBorderUIResource

A compound border UI resource.

static class

BorderUIResource.EmptyBorderUIResource

An empty border UI resource.

static class

BorderUIResource.EtchedBorderUIResource

An etched border UI resource.

static class

BorderUIResource.LineBorderUIResource

A line border UI resource.

static class

BorderUIResource.MatteBorderUIResource

A matte border UI resource.

static class

BorderUIResource.TitledBorderUIResource

A titled border UI resource.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BorderUIResource

​(

Border

delegate)

Creates a UIResource border object which wraps
an existing Border instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Border

getBlackLineBorderUIResource

()

Returns a black line border UI resource.

static

Border

getEtchedBorderUIResource

()

Returns a etched border UI resource.

static

Border

getLoweredBevelBorderUIResource

()

Returns a lowered bevel border UI resource.

static

Border

getRaisedBevelBorderUIResource

()

Returns a raised bevel border UI resource.

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

- Methods declared in interface javax.swing.border.

Border

getBorderInsets

,

isBorderOpaque

,

paintBorder

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

BorderUIResource.BevelBorderUIResource

A bevel border UI resource.

static class

BorderUIResource.CompoundBorderUIResource

A compound border UI resource.

static class

BorderUIResource.EmptyBorderUIResource

An empty border UI resource.

static class

BorderUIResource.EtchedBorderUIResource

An etched border UI resource.

static class

BorderUIResource.LineBorderUIResource

A line border UI resource.

static class

BorderUIResource.MatteBorderUIResource

A matte border UI resource.

static class

BorderUIResource.TitledBorderUIResource

A titled border UI resource.

---

#### Nested Class Summary

A bevel border UI resource.

A compound border UI resource.

An empty border UI resource.

An etched border UI resource.

A line border UI resource.

A matte border UI resource.

A titled border UI resource.

Constructor Summary

Constructors

Constructor

Description

BorderUIResource

​(

Border

delegate)

Creates a UIResource border object which wraps
an existing Border instance.

---

#### Constructor Summary

Creates a UIResource border object which wraps
an existing Border instance.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Border

getBlackLineBorderUIResource

()

Returns a black line border UI resource.

static

Border

getEtchedBorderUIResource

()

Returns a etched border UI resource.

static

Border

getLoweredBevelBorderUIResource

()

Returns a lowered bevel border UI resource.

static

Border

getRaisedBevelBorderUIResource

()

Returns a raised bevel border UI resource.

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

- Methods declared in interface javax.swing.border.

Border

getBorderInsets

,

isBorderOpaque

,

paintBorder

---

#### Method Summary

Returns a black line border UI resource.

Returns a etched border UI resource.

Returns a lowered bevel border UI resource.

Returns a raised bevel border UI resource.

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

Methods declared in interface javax.swing.border.

Border

getBorderInsets

,

isBorderOpaque

,

paintBorder

---

#### Methods declared in interface javax.swing.border. Border

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BorderUIResource

```java
public BorderUIResource​(
Border
delegate)
```

Creates a UIResource border object which wraps
an existing Border instance.

**Parameters:** delegate

- the border being wrapped

============ METHOD DETAIL ==========

- Method Detail

- getEtchedBorderUIResource

```java
public static
Border
getEtchedBorderUIResource()
```

Returns a etched border UI resource.

**Returns:** a etched border UI resource

- getLoweredBevelBorderUIResource

```java
public static
Border
getLoweredBevelBorderUIResource()
```

Returns a lowered bevel border UI resource.

**Returns:** a lowered bevel border UI resource

- getRaisedBevelBorderUIResource

```java
public static
Border
getRaisedBevelBorderUIResource()
```

Returns a raised bevel border UI resource.

**Returns:** a raised bevel border UI resource

- getBlackLineBorderUIResource

```java
public static
Border
getBlackLineBorderUIResource()
```

Returns a black line border UI resource.

**Returns:** a black line border UI resource

Constructor Detail

- BorderUIResource

```java
public BorderUIResource​(
Border
delegate)
```

Creates a UIResource border object which wraps
an existing Border instance.

**Parameters:** delegate

- the border being wrapped

---

#### Constructor Detail

BorderUIResource

```java
public BorderUIResource​(
Border
delegate)
```

Creates a UIResource border object which wraps
an existing Border instance.

**Parameters:** delegate

- the border being wrapped

---

#### BorderUIResource

public BorderUIResource​(

Border

delegate)

Creates a UIResource border object which wraps
an existing Border instance.

Method Detail

- getEtchedBorderUIResource

```java
public static
Border
getEtchedBorderUIResource()
```

Returns a etched border UI resource.

**Returns:** a etched border UI resource

- getLoweredBevelBorderUIResource

```java
public static
Border
getLoweredBevelBorderUIResource()
```

Returns a lowered bevel border UI resource.

**Returns:** a lowered bevel border UI resource

- getRaisedBevelBorderUIResource

```java
public static
Border
getRaisedBevelBorderUIResource()
```

Returns a raised bevel border UI resource.

**Returns:** a raised bevel border UI resource

- getBlackLineBorderUIResource

```java
public static
Border
getBlackLineBorderUIResource()
```

Returns a black line border UI resource.

**Returns:** a black line border UI resource

---

#### Method Detail

getEtchedBorderUIResource

```java
public static
Border
getEtchedBorderUIResource()
```

Returns a etched border UI resource.

**Returns:** a etched border UI resource

---

#### getEtchedBorderUIResource

public static

Border

getEtchedBorderUIResource()

Returns a etched border UI resource.

getLoweredBevelBorderUIResource

```java
public static
Border
getLoweredBevelBorderUIResource()
```

Returns a lowered bevel border UI resource.

**Returns:** a lowered bevel border UI resource

---

#### getLoweredBevelBorderUIResource

public static

Border

getLoweredBevelBorderUIResource()

Returns a lowered bevel border UI resource.

getRaisedBevelBorderUIResource

```java
public static
Border
getRaisedBevelBorderUIResource()
```

Returns a raised bevel border UI resource.

**Returns:** a raised bevel border UI resource

---

#### getRaisedBevelBorderUIResource

public static

Border

getRaisedBevelBorderUIResource()

Returns a raised bevel border UI resource.

getBlackLineBorderUIResource

```java
public static
Border
getBlackLineBorderUIResource()
```

Returns a black line border UI resource.

**Returns:** a black line border UI resource

---

#### getBlackLineBorderUIResource

public static

Border

getBlackLineBorderUIResource()

Returns a black line border UI resource.

---

