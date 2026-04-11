# Class MissingResourceException

**Source:** `java.base\java\util\MissingResourceException.html`

### Class Description

```java
public class
MissingResourceException

extends
RuntimeException
```

Signals that a resource is missing.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MissingResourceException​(
String
s,

String
className,

String
key)

Constructs a MissingResourceException with the specified information.
A detail message is a String that describes this particular exception.

**Parameters:**
- s

- the detail message
- className

- the name of the resource class
- key

- the key for the missing resource.

---

### Method Details

#### public
String
getClassName()

Gets parameter passed by constructor.

**Returns:**
- the name of the resource class

---

#### public
String
getKey()

Gets parameter passed by constructor.

**Returns:**
- the key for the missing resource

---

### Additional Sections

#### Class MissingResourceException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.util.MissingResourceException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.util.MissingResourceException

java.lang.Exception

- java.lang.RuntimeException
- - java.util.MissingResourceException

java.lang.RuntimeException

- java.util.MissingResourceException

java.util.MissingResourceException

**All Implemented Interfaces:** Serializable

```java
public class
MissingResourceException

extends
RuntimeException
```

Signals that a resource is missing.

**Since:** 1.1
**See Also:** Exception

,

ResourceBundle

,

Serialized Form

public class

MissingResourceException

extends

RuntimeException

Signals that a resource is missing.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MissingResourceException

​(

String

s,

String

className,

String

key)

Constructs a MissingResourceException with the specified information.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getClassName

()

Gets parameter passed by constructor.

String

getKey

()

Gets parameter passed by constructor.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Constructor Summary

Constructors

Constructor

Description

MissingResourceException

​(

String

s,

String

className,

String

key)

Constructs a MissingResourceException with the specified information.

---

#### Constructor Summary

Constructs a MissingResourceException with the specified information.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getClassName

()

Gets parameter passed by constructor.

String

getKey

()

Gets parameter passed by constructor.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Gets parameter passed by constructor.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MissingResourceException

```java
public MissingResourceException​(
String
s,

String
className,

String
key)
```

Constructs a MissingResourceException with the specified information.
A detail message is a String that describes this particular exception.

**Parameters:** s

- the detail message
**Parameters:** className

- the name of the resource class
**Parameters:** key

- the key for the missing resource.

============ METHOD DETAIL ==========

- Method Detail

- getClassName

```java
public
String
getClassName()
```

Gets parameter passed by constructor.

**Returns:** the name of the resource class

- getKey

```java
public
String
getKey()
```

Gets parameter passed by constructor.

**Returns:** the key for the missing resource

Constructor Detail

- MissingResourceException

```java
public MissingResourceException​(
String
s,

String
className,

String
key)
```

Constructs a MissingResourceException with the specified information.
A detail message is a String that describes this particular exception.

**Parameters:** s

- the detail message
**Parameters:** className

- the name of the resource class
**Parameters:** key

- the key for the missing resource.

---

#### Constructor Detail

MissingResourceException

```java
public MissingResourceException​(
String
s,

String
className,

String
key)
```

Constructs a MissingResourceException with the specified information.
A detail message is a String that describes this particular exception.

**Parameters:** s

- the detail message
**Parameters:** className

- the name of the resource class
**Parameters:** key

- the key for the missing resource.

---

#### MissingResourceException

public MissingResourceException​(

String

s,

String

className,

String

key)

Constructs a MissingResourceException with the specified information.
A detail message is a String that describes this particular exception.

Method Detail

- getClassName

```java
public
String
getClassName()
```

Gets parameter passed by constructor.

**Returns:** the name of the resource class

- getKey

```java
public
String
getKey()
```

Gets parameter passed by constructor.

**Returns:** the key for the missing resource

---

#### Method Detail

getClassName

```java
public
String
getClassName()
```

Gets parameter passed by constructor.

**Returns:** the name of the resource class

---

#### getClassName

public

String

getClassName()

Gets parameter passed by constructor.

getKey

```java
public
String
getKey()
```

Gets parameter passed by constructor.

**Returns:** the key for the missing resource

---

#### getKey

public

String

getKey()

Gets parameter passed by constructor.

---

