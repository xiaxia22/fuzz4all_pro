# Interface Connector.BooleanArgument

**Source:** `jdk.jdi\com\sun\jdi\connect\Connector.BooleanArgument.html`

### Class Description

```java
public static interface
Connector.BooleanArgument

extends
Connector.Argument
```

Specification for and value of a Connector argument,
whose value is Boolean. Boolean values are represented
by the localized versions of the strings "true" and "false".

**All Superinterfaces:** Connector.Argument

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setValue​(boolean value)

Sets the value of the argument.

---

#### boolean isValid​(
String
value)

Performs basic sanity check of argument.

**Specified by:**
- isValid

in interface

Connector.Argument

**Returns:**
- true

if value is a string
representation of a boolean value.

**See Also:**
- stringValueOf(boolean)

---

#### String
stringValueOf​(boolean value)

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

**Returns:**
- the localized String representation of the
boolean value.

---

#### boolean booleanValue()

Return the value of the argument as a boolean. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the boolean returned by this method is undefined.

**Returns:**
- the value of the argument as a boolean.

---

### Additional Sections

#### Interface Connector.BooleanArgument

**All Superinterfaces:** Connector.Argument

,

Serializable

**Enclosing interface:** Connector

```java
public static interface
Connector.BooleanArgument

extends
Connector.Argument
```

Specification for and value of a Connector argument,
whose value is Boolean. Boolean values are represented
by the localized versions of the strings "true" and "false".

public static interface

Connector.BooleanArgument

extends

Connector.Argument

Specification for and value of a Connector argument,
whose value is Boolean. Boolean values are represented
by the localized versions of the strings "true" and "false".

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

booleanValue

()

Return the value of the argument as a boolean.

boolean

isValid

​(

String

value)

Performs basic sanity check of argument.

void

setValue

​(boolean value)

Sets the value of the argument.

String

stringValueOf

​(boolean value)

Return the string representation of the

value

parameter.

- Methods declared in interface com.sun.jdi.connect.

Connector.Argument

description

,

label

,

mustSpecify

,

name

,

setValue

,

value

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

booleanValue

()

Return the value of the argument as a boolean.

boolean

isValid

​(

String

value)

Performs basic sanity check of argument.

void

setValue

​(boolean value)

Sets the value of the argument.

String

stringValueOf

​(boolean value)

Return the string representation of the

value

parameter.

- Methods declared in interface com.sun.jdi.connect.

Connector.Argument

description

,

label

,

mustSpecify

,

name

,

setValue

,

value

---

#### Method Summary

Return the value of the argument as a boolean.

Performs basic sanity check of argument.

Sets the value of the argument.

Return the string representation of the

value

parameter.

Methods declared in interface com.sun.jdi.connect.

Connector.Argument

description

,

label

,

mustSpecify

,

name

,

setValue

,

value

---

#### Methods declared in interface com.sun.jdi.connect. Connector.Argument

============ METHOD DETAIL ==========

- Method Detail

- setValue

```java
void setValue​(boolean value)
```

Sets the value of the argument.

- isValid

```java
boolean isValid​(
String
value)
```

Performs basic sanity check of argument.

**Specified by:** isValid

in interface

Connector.Argument
**Returns:** true

if value is a string
representation of a boolean value.
**See Also:** stringValueOf(boolean)

- stringValueOf

```java
String
stringValueOf​(boolean value)
```

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

**Returns:** the localized String representation of the
boolean value.

- booleanValue

```java
boolean booleanValue()
```

Return the value of the argument as a boolean. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the boolean returned by this method is undefined.

**Returns:** the value of the argument as a boolean.

Method Detail

- setValue

```java
void setValue​(boolean value)
```

Sets the value of the argument.

- isValid

```java
boolean isValid​(
String
value)
```

Performs basic sanity check of argument.

**Specified by:** isValid

in interface

Connector.Argument
**Returns:** true

if value is a string
representation of a boolean value.
**See Also:** stringValueOf(boolean)

- stringValueOf

```java
String
stringValueOf​(boolean value)
```

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

**Returns:** the localized String representation of the
boolean value.

- booleanValue

```java
boolean booleanValue()
```

Return the value of the argument as a boolean. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the boolean returned by this method is undefined.

**Returns:** the value of the argument as a boolean.

---

#### Method Detail

setValue

```java
void setValue​(boolean value)
```

Sets the value of the argument.

---

#### setValue

void setValue​(boolean value)

Sets the value of the argument.

isValid

```java
boolean isValid​(
String
value)
```

Performs basic sanity check of argument.

**Specified by:** isValid

in interface

Connector.Argument
**Returns:** true

if value is a string
representation of a boolean value.
**See Also:** stringValueOf(boolean)

---

#### isValid

boolean isValid​(

String

value)

Performs basic sanity check of argument.

stringValueOf

```java
String
stringValueOf​(boolean value)
```

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

**Returns:** the localized String representation of the
boolean value.

---

#### stringValueOf

String

stringValueOf​(boolean value)

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

booleanValue

```java
boolean booleanValue()
```

Return the value of the argument as a boolean. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the boolean returned by this method is undefined.

**Returns:** the value of the argument as a boolean.

---

#### booleanValue

boolean booleanValue()

Return the value of the argument as a boolean. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the boolean returned by this method is undefined.

---

