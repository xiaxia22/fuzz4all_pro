# Class RecordedFrame

**Source:** `jdk.jfr\jdk\jfr\consumer\RecordedFrame.html`

### Class Description

```java
public final class
RecordedFrame

extends
RecordedObject
```

A recorded frame in a stack trace.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public boolean isJavaFrame()

Returns

true

if this is a Java frame,

false

otherwise.

A Java method that has a native modifier is considered a Java frame.

**Returns:**
- true

if this is a Java frame,

false

otherwise

**See Also:**
- Modifier.isNative(int)

---

#### public int getBytecodeIndex()

Returns the bytecode index for the execution point that is represented by
this recorded frame.

**Returns:**
- byte code index, or

-1

if doesn't exist

---

#### public int getLineNumber()

Returns the line number for the execution point that is represented by this
recorded frame, or

-1

if doesn't exist

**Returns:**
- the line number, or

-1

if doesn't exist

---

#### public
String
getType()

Returns the frame type for the execution point that is represented by this
recorded frame (for example,

"Interpreted"

,

"JIT compiled"

or

"Inlined"

).

**Returns:**
- the frame type, or

null

if doesn't exist

---

#### public
RecordedMethod
getMethod()

Returns the method for the execution point that is represented by this
recorded frame.

**Returns:**
- the method, not

null

---

### Additional Sections

#### Class RecordedFrame

java.lang.Object

- jdk.jfr.consumer.RecordedObject
- - jdk.jfr.consumer.RecordedFrame

jdk.jfr.consumer.RecordedObject

- jdk.jfr.consumer.RecordedFrame

jdk.jfr.consumer.RecordedFrame

```java
public final class
RecordedFrame

extends
RecordedObject
```

A recorded frame in a stack trace.

**Since:** 9

public final class

RecordedFrame

extends

RecordedObject

A recorded frame in a stack trace.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getBytecodeIndex

()

Returns the bytecode index for the execution point that is represented by
this recorded frame.

int

getLineNumber

()

Returns the line number for the execution point that is represented by this
recorded frame, or

-1

if doesn't exist

RecordedMethod

getMethod

()

Returns the method for the execution point that is represented by this
recorded frame.

String

getType

()

Returns the frame type for the execution point that is represented by this
recorded frame (for example,

"Interpreted"

,

"JIT compiled"

or

"Inlined"

).

boolean

isJavaFrame

()

Returns

true

if this is a Java frame,

false

otherwise.

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

int

getBytecodeIndex

()

Returns the bytecode index for the execution point that is represented by
this recorded frame.

int

getLineNumber

()

Returns the line number for the execution point that is represented by this
recorded frame, or

-1

if doesn't exist

RecordedMethod

getMethod

()

Returns the method for the execution point that is represented by this
recorded frame.

String

getType

()

Returns the frame type for the execution point that is represented by this
recorded frame (for example,

"Interpreted"

,

"JIT compiled"

or

"Inlined"

).

boolean

isJavaFrame

()

Returns

true

if this is a Java frame,

false

otherwise.

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

Returns the bytecode index for the execution point that is represented by
this recorded frame.

Returns the line number for the execution point that is represented by this
recorded frame, or

-1

if doesn't exist

Returns the method for the execution point that is represented by this
recorded frame.

Returns the frame type for the execution point that is represented by this
recorded frame (for example,

"Interpreted"

,

"JIT compiled"

or

"Inlined"

).

Returns

true

if this is a Java frame,

false

otherwise.

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

- isJavaFrame

```java
public boolean isJavaFrame()
```

Returns

true

if this is a Java frame,

false

otherwise.

A Java method that has a native modifier is considered a Java frame.

**Returns:** true

if this is a Java frame,

false

otherwise
**See Also:** Modifier.isNative(int)

- getBytecodeIndex

```java
public int getBytecodeIndex()
```

Returns the bytecode index for the execution point that is represented by
this recorded frame.

**Returns:** byte code index, or

-1

if doesn't exist

- getLineNumber

```java
public int getLineNumber()
```

Returns the line number for the execution point that is represented by this
recorded frame, or

-1

if doesn't exist

**Returns:** the line number, or

-1

if doesn't exist

- getType

```java
public
String
getType()
```

Returns the frame type for the execution point that is represented by this
recorded frame (for example,

"Interpreted"

,

"JIT compiled"

or

"Inlined"

).

**Returns:** the frame type, or

null

if doesn't exist

- getMethod

```java
public
RecordedMethod
getMethod()
```

Returns the method for the execution point that is represented by this
recorded frame.

**Returns:** the method, not

null

Method Detail

- isJavaFrame

```java
public boolean isJavaFrame()
```

Returns

true

if this is a Java frame,

false

otherwise.

A Java method that has a native modifier is considered a Java frame.

**Returns:** true

if this is a Java frame,

false

otherwise
**See Also:** Modifier.isNative(int)

- getBytecodeIndex

```java
public int getBytecodeIndex()
```

Returns the bytecode index for the execution point that is represented by
this recorded frame.

**Returns:** byte code index, or

-1

if doesn't exist

- getLineNumber

```java
public int getLineNumber()
```

Returns the line number for the execution point that is represented by this
recorded frame, or

-1

if doesn't exist

**Returns:** the line number, or

-1

if doesn't exist

- getType

```java
public
String
getType()
```

Returns the frame type for the execution point that is represented by this
recorded frame (for example,

"Interpreted"

,

"JIT compiled"

or

"Inlined"

).

**Returns:** the frame type, or

null

if doesn't exist

- getMethod

```java
public
RecordedMethod
getMethod()
```

Returns the method for the execution point that is represented by this
recorded frame.

**Returns:** the method, not

null

---

#### Method Detail

isJavaFrame

```java
public boolean isJavaFrame()
```

Returns

true

if this is a Java frame,

false

otherwise.

A Java method that has a native modifier is considered a Java frame.

**Returns:** true

if this is a Java frame,

false

otherwise
**See Also:** Modifier.isNative(int)

---

#### isJavaFrame

public boolean isJavaFrame()

Returns

true

if this is a Java frame,

false

otherwise.

A Java method that has a native modifier is considered a Java frame.

A Java method that has a native modifier is considered a Java frame.

getBytecodeIndex

```java
public int getBytecodeIndex()
```

Returns the bytecode index for the execution point that is represented by
this recorded frame.

**Returns:** byte code index, or

-1

if doesn't exist

---

#### getBytecodeIndex

public int getBytecodeIndex()

Returns the bytecode index for the execution point that is represented by
this recorded frame.

getLineNumber

```java
public int getLineNumber()
```

Returns the line number for the execution point that is represented by this
recorded frame, or

-1

if doesn't exist

**Returns:** the line number, or

-1

if doesn't exist

---

#### getLineNumber

public int getLineNumber()

Returns the line number for the execution point that is represented by this
recorded frame, or

-1

if doesn't exist

getType

```java
public
String
getType()
```

Returns the frame type for the execution point that is represented by this
recorded frame (for example,

"Interpreted"

,

"JIT compiled"

or

"Inlined"

).

**Returns:** the frame type, or

null

if doesn't exist

---

#### getType

public

String

getType()

Returns the frame type for the execution point that is represented by this
recorded frame (for example,

"Interpreted"

,

"JIT compiled"

or

"Inlined"

).

getMethod

```java
public
RecordedMethod
getMethod()
```

Returns the method for the execution point that is represented by this
recorded frame.

**Returns:** the method, not

null

---

#### getMethod

public

RecordedMethod

getMethod()

Returns the method for the execution point that is represented by this
recorded frame.

---

