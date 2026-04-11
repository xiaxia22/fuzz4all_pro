# Class RecordedMethod

**Source:** `jdk.jfr\jdk\jfr\consumer\RecordedMethod.html`

### Class Description

```java
public final class
RecordedMethod

extends
RecordedObject
```

A recorded method.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
RecordedClass
getType()

Returns the class this method belongs to, if it belong to a Java frame.

To ensure this is a Java frame, use the

RecordedFrame.isJavaFrame()

method.

**Returns:**
- the class, may be

null

if not a Java frame

**See Also:**
- RecordedFrame.isJavaFrame()

---

#### public
String
getName()

Returns the name of this method, for example

"toString"

.

If this method doesn't belong to a Java frame the result is undefined.

**Returns:**
- method name, or

null

if doesn't exist

**See Also:**
- RecordedFrame.isJavaFrame()

---

#### public
String
getDescriptor()

Returns the method descriptor for this method (for example,

"(Ljava/lang/String;)V"

).

See Java Virtual Machine Specification, 4.3

If this method doesn't belong to a Java frame then the the result is undefined.

**Returns:**
- method descriptor.

**See Also:**
- RecordedFrame.isJavaFrame()

---

#### public int getModifiers()

Returns the modifiers for this method.

If this method doesn't belong to a Java frame, then the result is undefined.

**Returns:**
- the modifiers

**See Also:**
- Modifier

,

RecordedFrame.isJavaFrame()

---

#### public boolean isHidden()

Returns whether this method is hidden (for example, wrapper code in a lambda
expressions).

**Returns:**
- true

if method is hidden,

false

otherwise

---

### Additional Sections

#### Class RecordedMethod

java.lang.Object

- jdk.jfr.consumer.RecordedObject
- - jdk.jfr.consumer.RecordedMethod

jdk.jfr.consumer.RecordedObject

- jdk.jfr.consumer.RecordedMethod

jdk.jfr.consumer.RecordedMethod

```java
public final class
RecordedMethod

extends
RecordedObject
```

A recorded method.

**Since:** 9

public final class

RecordedMethod

extends

RecordedObject

A recorded method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDescriptor

()

Returns the method descriptor for this method (for example,

"(Ljava/lang/String;)V"

).

int

getModifiers

()

Returns the modifiers for this method.

String

getName

()

Returns the name of this method, for example

"toString"

.

RecordedClass

getType

()

Returns the class this method belongs to, if it belong to a Java frame.

boolean

isHidden

()

Returns whether this method is hidden (for example, wrapper code in a lambda
expressions).

- Methods declared in class jdk.jfr.consumer.

RecordedObject

getBoolean

,

getByte

,

getChar

,

getClass

,

getDouble

,

getDuration

,

getFields

,

getFloat

,

getInstant

,

getInt

,

getLong

,

getShort

,

getString

,

getThread

,

getValue

,

hasField

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDescriptor

()

Returns the method descriptor for this method (for example,

"(Ljava/lang/String;)V"

).

int

getModifiers

()

Returns the modifiers for this method.

String

getName

()

Returns the name of this method, for example

"toString"

.

RecordedClass

getType

()

Returns the class this method belongs to, if it belong to a Java frame.

boolean

isHidden

()

Returns whether this method is hidden (for example, wrapper code in a lambda
expressions).

- Methods declared in class jdk.jfr.consumer.

RecordedObject

getBoolean

,

getByte

,

getChar

,

getClass

,

getDouble

,

getDuration

,

getFields

,

getFloat

,

getInstant

,

getInt

,

getLong

,

getShort

,

getString

,

getThread

,

getValue

,

hasField

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

Returns the method descriptor for this method (for example,

"(Ljava/lang/String;)V"

).

Returns the modifiers for this method.

Returns the name of this method, for example

"toString"

.

Returns the class this method belongs to, if it belong to a Java frame.

Returns whether this method is hidden (for example, wrapper code in a lambda
expressions).

Methods declared in class jdk.jfr.consumer.

RecordedObject

getBoolean

,

getByte

,

getChar

,

getClass

,

getDouble

,

getDuration

,

getFields

,

getFloat

,

getInstant

,

getInt

,

getLong

,

getShort

,

getString

,

getThread

,

getValue

,

hasField

,

toString

---

#### Methods declared in class jdk.jfr.consumer. RecordedObject

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

- getType

```java
public
RecordedClass
getType()
```

Returns the class this method belongs to, if it belong to a Java frame.

To ensure this is a Java frame, use the

RecordedFrame.isJavaFrame()

method.

**Returns:** the class, may be

null

if not a Java frame
**See Also:** RecordedFrame.isJavaFrame()

- getName

```java
public
String
getName()
```

Returns the name of this method, for example

"toString"

.

If this method doesn't belong to a Java frame the result is undefined.

**Returns:** method name, or

null

if doesn't exist
**See Also:** RecordedFrame.isJavaFrame()

- getDescriptor

```java
public
String
getDescriptor()
```

Returns the method descriptor for this method (for example,

"(Ljava/lang/String;)V"

).

See Java Virtual Machine Specification, 4.3

If this method doesn't belong to a Java frame then the the result is undefined.

**Returns:** method descriptor.
**See Also:** RecordedFrame.isJavaFrame()

- getModifiers

```java
public int getModifiers()
```

Returns the modifiers for this method.

If this method doesn't belong to a Java frame, then the result is undefined.

**Returns:** the modifiers
**See Also:** Modifier

,

RecordedFrame.isJavaFrame()

- isHidden

```java
public boolean isHidden()
```

Returns whether this method is hidden (for example, wrapper code in a lambda
expressions).

**Returns:** true

if method is hidden,

false

otherwise

Method Detail

- getType

```java
public
RecordedClass
getType()
```

Returns the class this method belongs to, if it belong to a Java frame.

To ensure this is a Java frame, use the

RecordedFrame.isJavaFrame()

method.

**Returns:** the class, may be

null

if not a Java frame
**See Also:** RecordedFrame.isJavaFrame()

- getName

```java
public
String
getName()
```

Returns the name of this method, for example

"toString"

.

If this method doesn't belong to a Java frame the result is undefined.

**Returns:** method name, or

null

if doesn't exist
**See Also:** RecordedFrame.isJavaFrame()

- getDescriptor

```java
public
String
getDescriptor()
```

Returns the method descriptor for this method (for example,

"(Ljava/lang/String;)V"

).

See Java Virtual Machine Specification, 4.3

If this method doesn't belong to a Java frame then the the result is undefined.

**Returns:** method descriptor.
**See Also:** RecordedFrame.isJavaFrame()

- getModifiers

```java
public int getModifiers()
```

Returns the modifiers for this method.

If this method doesn't belong to a Java frame, then the result is undefined.

**Returns:** the modifiers
**See Also:** Modifier

,

RecordedFrame.isJavaFrame()

- isHidden

```java
public boolean isHidden()
```

Returns whether this method is hidden (for example, wrapper code in a lambda
expressions).

**Returns:** true

if method is hidden,

false

otherwise

---

#### Method Detail

getType

```java
public
RecordedClass
getType()
```

Returns the class this method belongs to, if it belong to a Java frame.

To ensure this is a Java frame, use the

RecordedFrame.isJavaFrame()

method.

**Returns:** the class, may be

null

if not a Java frame
**See Also:** RecordedFrame.isJavaFrame()

---

#### getType

public

RecordedClass

getType()

Returns the class this method belongs to, if it belong to a Java frame.

To ensure this is a Java frame, use the

RecordedFrame.isJavaFrame()

method.

To ensure this is a Java frame, use the

RecordedFrame.isJavaFrame()

method.

getName

```java
public
String
getName()
```

Returns the name of this method, for example

"toString"

.

If this method doesn't belong to a Java frame the result is undefined.

**Returns:** method name, or

null

if doesn't exist
**See Also:** RecordedFrame.isJavaFrame()

---

#### getName

public

String

getName()

Returns the name of this method, for example

"toString"

.

If this method doesn't belong to a Java frame the result is undefined.

If this method doesn't belong to a Java frame the result is undefined.

getDescriptor

```java
public
String
getDescriptor()
```

Returns the method descriptor for this method (for example,

"(Ljava/lang/String;)V"

).

See Java Virtual Machine Specification, 4.3

If this method doesn't belong to a Java frame then the the result is undefined.

**Returns:** method descriptor.
**See Also:** RecordedFrame.isJavaFrame()

---

#### getDescriptor

public

String

getDescriptor()

Returns the method descriptor for this method (for example,

"(Ljava/lang/String;)V"

).

See Java Virtual Machine Specification, 4.3

If this method doesn't belong to a Java frame then the the result is undefined.

See Java Virtual Machine Specification, 4.3

If this method doesn't belong to a Java frame then the the result is undefined.

If this method doesn't belong to a Java frame then the the result is undefined.

getModifiers

```java
public int getModifiers()
```

Returns the modifiers for this method.

If this method doesn't belong to a Java frame, then the result is undefined.

**Returns:** the modifiers
**See Also:** Modifier

,

RecordedFrame.isJavaFrame()

---

#### getModifiers

public int getModifiers()

Returns the modifiers for this method.

If this method doesn't belong to a Java frame, then the result is undefined.

If this method doesn't belong to a Java frame, then the result is undefined.

isHidden

```java
public boolean isHidden()
```

Returns whether this method is hidden (for example, wrapper code in a lambda
expressions).

**Returns:** true

if method is hidden,

false

otherwise

---

#### isHidden

public boolean isHidden()

Returns whether this method is hidden (for example, wrapper code in a lambda
expressions).

---

