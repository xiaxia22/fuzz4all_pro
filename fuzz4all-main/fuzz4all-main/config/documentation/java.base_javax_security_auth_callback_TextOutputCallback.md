# Class TextOutputCallback

**Source:** `java.base\javax\security\auth\callback\TextOutputCallback.html`

### Class Description

```java
public class
TextOutputCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

TextOutputCallback

to the

handle

method of a

CallbackHandler

to display information messages,
warning messages and error messages.

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

#### public static final int INFORMATION

Information message.

**See Also:**
- Constant Field Values

---

#### public static final int WARNING

Warning message.

**See Also:**
- Constant Field Values

---

#### public static final int ERROR

Error message.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public TextOutputCallback​(int messageType,

String
message)

Construct a TextOutputCallback with a message type and message
to be displayed.

**Parameters:**
- messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
- message

- the message to be displayed.

**Throws:**
- IllegalArgumentException

- if

messageType

is not either

INFORMATION

,

WARNING

or

ERROR

,
if

message

is null,
or if

message

has a length of 0.

---

### Method Details

#### public int getMessageType()

Get the message type.

**Returns:**
- the message type (

INFORMATION

,

WARNING

or

ERROR

).

---

#### public
String
getMessage()

Get the message to be displayed.

**Returns:**
- the message to be displayed.

---

### Additional Sections

#### Class TextOutputCallback

java.lang.Object

- javax.security.auth.callback.TextOutputCallback

javax.security.auth.callback.TextOutputCallback

**All Implemented Interfaces:** Serializable

,

Callback

```java
public class
TextOutputCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

TextOutputCallback

to the

handle

method of a

CallbackHandler

to display information messages,
warning messages and error messages.

**Since:** 1.4
**See Also:** CallbackHandler

,

Serialized Form

public class

TextOutputCallback

extends

Object

implements

Callback

,

Serializable

Underlying security services instantiate and pass a

TextOutputCallback

to the

handle

method of a

CallbackHandler

to display information messages,
warning messages and error messages.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ERROR

Error message.

static int

INFORMATION

Information message.

static int

WARNING

Warning message.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TextOutputCallback

​(int messageType,

String

message)

Construct a TextOutputCallback with a message type and message
to be displayed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMessage

()

Get the message to be displayed.

int

getMessageType

()

Get the message type.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

ERROR

Error message.

static int

INFORMATION

Information message.

static int

WARNING

Warning message.

---

#### Field Summary

Error message.

Information message.

Warning message.

Constructor Summary

Constructors

Constructor

Description

TextOutputCallback

​(int messageType,

String

message)

Construct a TextOutputCallback with a message type and message
to be displayed.

---

#### Constructor Summary

Construct a TextOutputCallback with a message type and message
to be displayed.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMessage

()

Get the message to be displayed.

int

getMessageType

()

Get the message type.

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

Get the message to be displayed.

Get the message type.

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

============ FIELD DETAIL ===========

- Field Detail

- INFORMATION

```java
public static final int INFORMATION
```

Information message.

**See Also:** Constant Field Values

- WARNING

```java
public static final int WARNING
```

Warning message.

**See Also:** Constant Field Values

- ERROR

```java
public static final int ERROR
```

Error message.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TextOutputCallback

```java
public TextOutputCallback​(int messageType,

String
message)
```

Construct a TextOutputCallback with a message type and message
to be displayed.

**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** message

- the message to be displayed.
**Throws:** IllegalArgumentException

- if

messageType

is not either

INFORMATION

,

WARNING

or

ERROR

,
if

message

is null,
or if

message

has a length of 0.

============ METHOD DETAIL ==========

- Method Detail

- getMessageType

```java
public int getMessageType()
```

Get the message type.

**Returns:** the message type (

INFORMATION

,

WARNING

or

ERROR

).

- getMessage

```java
public
String
getMessage()
```

Get the message to be displayed.

**Returns:** the message to be displayed.

Field Detail

- INFORMATION

```java
public static final int INFORMATION
```

Information message.

**See Also:** Constant Field Values

- WARNING

```java
public static final int WARNING
```

Warning message.

**See Also:** Constant Field Values

- ERROR

```java
public static final int ERROR
```

Error message.

**See Also:** Constant Field Values

---

#### Field Detail

INFORMATION

```java
public static final int INFORMATION
```

Information message.

**See Also:** Constant Field Values

---

#### INFORMATION

public static final int INFORMATION

Information message.

WARNING

```java
public static final int WARNING
```

Warning message.

**See Also:** Constant Field Values

---

#### WARNING

public static final int WARNING

Warning message.

ERROR

```java
public static final int ERROR
```

Error message.

**See Also:** Constant Field Values

---

#### ERROR

public static final int ERROR

Error message.

Constructor Detail

- TextOutputCallback

```java
public TextOutputCallback​(int messageType,

String
message)
```

Construct a TextOutputCallback with a message type and message
to be displayed.

**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** message

- the message to be displayed.
**Throws:** IllegalArgumentException

- if

messageType

is not either

INFORMATION

,

WARNING

or

ERROR

,
if

message

is null,
or if

message

has a length of 0.

---

#### Constructor Detail

TextOutputCallback

```java
public TextOutputCallback​(int messageType,

String
message)
```

Construct a TextOutputCallback with a message type and message
to be displayed.

**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** message

- the message to be displayed.
**Throws:** IllegalArgumentException

- if

messageType

is not either

INFORMATION

,

WARNING

or

ERROR

,
if

message

is null,
or if

message

has a length of 0.

---

#### TextOutputCallback

public TextOutputCallback​(int messageType,

String

message)

Construct a TextOutputCallback with a message type and message
to be displayed.

Method Detail

- getMessageType

```java
public int getMessageType()
```

Get the message type.

**Returns:** the message type (

INFORMATION

,

WARNING

or

ERROR

).

- getMessage

```java
public
String
getMessage()
```

Get the message to be displayed.

**Returns:** the message to be displayed.

---

#### Method Detail

getMessageType

```java
public int getMessageType()
```

Get the message type.

**Returns:** the message type (

INFORMATION

,

WARNING

or

ERROR

).

---

#### getMessageType

public int getMessageType()

Get the message type.

getMessage

```java
public
String
getMessage()
```

Get the message to be displayed.

**Returns:** the message to be displayed.

---

#### getMessage

public

String

getMessage()

Get the message to be displayed.

---

