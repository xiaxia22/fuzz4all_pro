# Interface Connector.IntegerArgument

**Source:** `jdk.jdi\com\sun\jdi\connect\Connector.IntegerArgument.html`

### Class Description

```java
public static interface
Connector.IntegerArgument

extends
Connector.Argument
```

Specification for and value of a Connector argument,
whose value is an integer. Integer values are represented
by their corresponding strings.

**All Superinterfaces:** Connector.Argument

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setValue​(int value)

Sets the value of the argument.
The value should be checked with

isValid(int)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

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

if value represents an int that is

min()

<= value <=

max()

---

#### boolean isValid​(int value)

Performs basic sanity check of argument.

**Returns:**
- true

if

min()

<= value <=

max()

---

#### String
stringValueOf​(int value)

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

**Returns:**
- the String representation of the
int value.

---

#### int intValue()

Return the value of the argument as a int. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the int returned by this method is undefined.

**Returns:**
- the value of the argument as a int.

---

#### int max()

The upper bound for the value.

**Returns:**
- the maximum allowed value for this argument.

---

#### int min()

The lower bound for the value.

**Returns:**
- the minimum allowed value for this argument.

---

### Additional Sections

#### Interface Connector.IntegerArgument

**All Superinterfaces:** Connector.Argument

,

Serializable

**Enclosing interface:** Connector

```java
public static interface
Connector.IntegerArgument

extends
Connector.Argument
```

Specification for and value of a Connector argument,
whose value is an integer. Integer values are represented
by their corresponding strings.

public static interface

Connector.IntegerArgument

extends

Connector.Argument

Specification for and value of a Connector argument,
whose value is an integer. Integer values are represented
by their corresponding strings.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

intValue

()

Return the value of the argument as a int.

boolean

isValid

​(int value)

Performs basic sanity check of argument.

boolean

isValid

​(

String

value)

Performs basic sanity check of argument.

int

max

()

The upper bound for the value.

int

min

()

The lower bound for the value.

void

setValue

​(int value)

Sets the value of the argument.

String

stringValueOf

​(int value)

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

int

intValue

()

Return the value of the argument as a int.

boolean

isValid

​(int value)

Performs basic sanity check of argument.

boolean

isValid

​(

String

value)

Performs basic sanity check of argument.

int

max

()

The upper bound for the value.

int

min

()

The lower bound for the value.

void

setValue

​(int value)

Sets the value of the argument.

String

stringValueOf

​(int value)

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

Return the value of the argument as a int.

Performs basic sanity check of argument.

The upper bound for the value.

The lower bound for the value.

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
void setValue​(int value)
```

Sets the value of the argument.
The value should be checked with

isValid(int)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

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

if value represents an int that is

min()

<= value <=

max()

- isValid

```java
boolean isValid​(int value)
```

Performs basic sanity check of argument.

**Returns:** true

if

min()

<= value <=

max()

- stringValueOf

```java
String
stringValueOf​(int value)
```

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

**Returns:** the String representation of the
int value.

- intValue

```java
int intValue()
```

Return the value of the argument as a int. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the int returned by this method is undefined.

**Returns:** the value of the argument as a int.

- max

```java
int max()
```

The upper bound for the value.

**Returns:** the maximum allowed value for this argument.

- min

```java
int min()
```

The lower bound for the value.

**Returns:** the minimum allowed value for this argument.

Method Detail

- setValue

```java
void setValue​(int value)
```

Sets the value of the argument.
The value should be checked with

isValid(int)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

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

if value represents an int that is

min()

<= value <=

max()

- isValid

```java
boolean isValid​(int value)
```

Performs basic sanity check of argument.

**Returns:** true

if

min()

<= value <=

max()

- stringValueOf

```java
String
stringValueOf​(int value)
```

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

**Returns:** the String representation of the
int value.

- intValue

```java
int intValue()
```

Return the value of the argument as a int. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the int returned by this method is undefined.

**Returns:** the value of the argument as a int.

- max

```java
int max()
```

The upper bound for the value.

**Returns:** the maximum allowed value for this argument.

- min

```java
int min()
```

The lower bound for the value.

**Returns:** the minimum allowed value for this argument.

---

#### Method Detail

setValue

```java
void setValue​(int value)
```

Sets the value of the argument.
The value should be checked with

isValid(int)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

---

#### setValue

void setValue​(int value)

Sets the value of the argument.
The value should be checked with

isValid(int)

before setting it; invalid values will throw an exception
when the connection is established - for example,
on

LaunchingConnector.launch(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

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

if value represents an int that is

min()

<= value <=

max()

---

#### isValid

boolean isValid​(

String

value)

Performs basic sanity check of argument.

isValid

```java
boolean isValid​(int value)
```

Performs basic sanity check of argument.

**Returns:** true

if

min()

<= value <=

max()

---

#### isValid

boolean isValid​(int value)

Performs basic sanity check of argument.

stringValueOf

```java
String
stringValueOf​(int value)
```

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

**Returns:** the String representation of the
int value.

---

#### stringValueOf

String

stringValueOf​(int value)

Return the string representation of the

value

parameter.
Does not set or examine the current value of

this

instance.

intValue

```java
int intValue()
```

Return the value of the argument as a int. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the int returned by this method is undefined.

**Returns:** the value of the argument as a int.

---

#### intValue

int intValue()

Return the value of the argument as a int. Since
the argument may not have been set or may have an invalid
value

isValid(String)

should be called on

Connector.Argument.value()

to check its validity. If it is invalid
the int returned by this method is undefined.

max

```java
int max()
```

The upper bound for the value.

**Returns:** the maximum allowed value for this argument.

---

#### max

int max()

The upper bound for the value.

min

```java
int min()
```

The lower bound for the value.

**Returns:** the minimum allowed value for this argument.

---

#### min

int min()

The lower bound for the value.

---

