# Class IllegalFormatConversionException

**Source:** `java.base\java\util\IllegalFormatConversionException.html`

### Class Description

```java
public class
IllegalFormatConversionException

extends
IllegalFormatException
```

Unchecked exception thrown when the argument corresponding to the format
specifier is of an incompatible type.

Unless otherwise specified, passing a

null

argument to any
method or constructor in this class will cause a

NullPointerException

to be thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IllegalFormatConversionException​(char c,

Class
<?> arg)

Constructs an instance of this class with the mismatched conversion and
the corresponding argument class.

**Parameters:**
- c

- Inapplicable conversion
- arg

- Class of the mismatched argument

---

### Method Details

#### public char getConversion()

Returns the inapplicable conversion.

**Returns:**
- The inapplicable conversion

---

#### public
Class
<?> getArgumentClass()

Returns the class of the mismatched argument.

**Returns:**
- The class of the mismatched argument

---

### Additional Sections

#### Class IllegalFormatConversionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalArgumentException
- - java.util.IllegalFormatException
- - java.util.IllegalFormatConversionException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.IllegalArgumentException
- - java.util.IllegalFormatException
- - java.util.IllegalFormatConversionException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.IllegalArgumentException
- - java.util.IllegalFormatException
- - java.util.IllegalFormatConversionException

java.lang.RuntimeException

- java.lang.IllegalArgumentException
- - java.util.IllegalFormatException
- - java.util.IllegalFormatConversionException

java.lang.IllegalArgumentException

- java.util.IllegalFormatException
- - java.util.IllegalFormatConversionException

java.util.IllegalFormatException

- java.util.IllegalFormatConversionException

java.util.IllegalFormatConversionException

**All Implemented Interfaces:** Serializable

```java
public class
IllegalFormatConversionException

extends
IllegalFormatException
```

Unchecked exception thrown when the argument corresponding to the format
specifier is of an incompatible type.

Unless otherwise specified, passing a

null

argument to any
method or constructor in this class will cause a

NullPointerException

to be thrown.

**Since:** 1.5
**See Also:** Serialized Form

public class

IllegalFormatConversionException

extends

IllegalFormatException

Unchecked exception thrown when the argument corresponding to the format
specifier is of an incompatible type.

Unless otherwise specified, passing a

null

argument to any
method or constructor in this class will cause a

NullPointerException

to be thrown.

Unless otherwise specified, passing a

null

argument to any
method or constructor in this class will cause a

NullPointerException

to be thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IllegalFormatConversionException

​(char c,

Class

<?> arg)

Constructs an instance of this class with the mismatched conversion and
the corresponding argument class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getArgumentClass

()

Returns the class of the mismatched argument.

char

getConversion

()

Returns the inapplicable conversion.

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

IllegalFormatConversionException

​(char c,

Class

<?> arg)

Constructs an instance of this class with the mismatched conversion and
the corresponding argument class.

---

#### Constructor Summary

Constructs an instance of this class with the mismatched conversion and
the corresponding argument class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<?>

getArgumentClass

()

Returns the class of the mismatched argument.

char

getConversion

()

Returns the inapplicable conversion.

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

Returns the class of the mismatched argument.

Returns the inapplicable conversion.

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

- IllegalFormatConversionException

```java
public IllegalFormatConversionException​(char c,

Class
<?> arg)
```

Constructs an instance of this class with the mismatched conversion and
the corresponding argument class.

**Parameters:** c

- Inapplicable conversion
**Parameters:** arg

- Class of the mismatched argument

============ METHOD DETAIL ==========

- Method Detail

- getConversion

```java
public char getConversion()
```

Returns the inapplicable conversion.

**Returns:** The inapplicable conversion

- getArgumentClass

```java
public
Class
<?> getArgumentClass()
```

Returns the class of the mismatched argument.

**Returns:** The class of the mismatched argument

Constructor Detail

- IllegalFormatConversionException

```java
public IllegalFormatConversionException​(char c,

Class
<?> arg)
```

Constructs an instance of this class with the mismatched conversion and
the corresponding argument class.

**Parameters:** c

- Inapplicable conversion
**Parameters:** arg

- Class of the mismatched argument

---

#### Constructor Detail

IllegalFormatConversionException

```java
public IllegalFormatConversionException​(char c,

Class
<?> arg)
```

Constructs an instance of this class with the mismatched conversion and
the corresponding argument class.

**Parameters:** c

- Inapplicable conversion
**Parameters:** arg

- Class of the mismatched argument

---

#### IllegalFormatConversionException

public IllegalFormatConversionException​(char c,

Class

<?> arg)

Constructs an instance of this class with the mismatched conversion and
the corresponding argument class.

Method Detail

- getConversion

```java
public char getConversion()
```

Returns the inapplicable conversion.

**Returns:** The inapplicable conversion

- getArgumentClass

```java
public
Class
<?> getArgumentClass()
```

Returns the class of the mismatched argument.

**Returns:** The class of the mismatched argument

---

#### Method Detail

getConversion

```java
public char getConversion()
```

Returns the inapplicable conversion.

**Returns:** The inapplicable conversion

---

#### getConversion

public char getConversion()

Returns the inapplicable conversion.

getArgumentClass

```java
public
Class
<?> getArgumentClass()
```

Returns the class of the mismatched argument.

**Returns:** The class of the mismatched argument

---

#### getArgumentClass

public

Class

<?> getArgumentClass()

Returns the class of the mismatched argument.

---

