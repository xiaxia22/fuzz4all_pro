# Interface Doclet.Option

**Source:** `jdk.javadoc\jdk\javadoc\doclet\Doclet.Option.html`

### Class Description

```java
public static interface
Doclet.Option
```

An encapsulation of option name, aliases, parameters and descriptions
as used by the Doclet.

**Enclosing interface:** Doclet

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getArgumentCount()

Returns the number of arguments, this option will consume.

**Returns:**
- number of consumed arguments

---

#### String
getDescription()

Returns the description of the option. For instance, the option "group", would
return the synopsis of the option such as, "groups the documents".

**Returns:**
- description if set, otherwise an empty String

---

#### Doclet.Option.Kind
getKind()

Returns the option kind.

**Returns:**
- the kind of this option

---

#### List
<
String
> getNames()

Returns the list of names that may be used to identify the option. For instance, the
list could be

["-classpath", "--class-path"]

for the
option "-classpath", with an alias "--class-path".

**Returns:**
- the names of the option

---

#### String
getParameters()

Returns the parameters of the option. For instance "name <p1>:<p2>.."

**Returns:**
- parameters if set, otherwise an empty String

---

#### boolean process​(
String
option,

List
<
String
> arguments)

Processes the option and arguments as needed. This method will
be invoked if the given option name matches the option.

**Parameters:**
- option

- the option
- arguments

- a list encapsulating the arguments

**Returns:**
- true if operation succeeded, false otherwise

---

### Additional Sections

#### Interface Doclet.Option

**Enclosing interface:** Doclet

```java
public static interface
Doclet.Option
```

An encapsulation of option name, aliases, parameters and descriptions
as used by the Doclet.

public static interface

Doclet.Option

An encapsulation of option name, aliases, parameters and descriptions
as used by the Doclet.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Doclet.Option.Kind

The kind of an option.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getArgumentCount

()

Returns the number of arguments, this option will consume.

String

getDescription

()

Returns the description of the option.

Doclet.Option.Kind

getKind

()

Returns the option kind.

List

<

String

>

getNames

()

Returns the list of names that may be used to identify the option.

String

getParameters

()

Returns the parameters of the option.

boolean

process

​(

String

option,

List

<

String

> arguments)

Processes the option and arguments as needed.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Doclet.Option.Kind

The kind of an option.

---

#### Nested Class Summary

The kind of an option.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getArgumentCount

()

Returns the number of arguments, this option will consume.

String

getDescription

()

Returns the description of the option.

Doclet.Option.Kind

getKind

()

Returns the option kind.

List

<

String

>

getNames

()

Returns the list of names that may be used to identify the option.

String

getParameters

()

Returns the parameters of the option.

boolean

process

​(

String

option,

List

<

String

> arguments)

Processes the option and arguments as needed.

---

#### Method Summary

Returns the number of arguments, this option will consume.

Returns the description of the option.

Returns the option kind.

Returns the list of names that may be used to identify the option.

Returns the parameters of the option.

Processes the option and arguments as needed.

============ METHOD DETAIL ==========

- Method Detail

- getArgumentCount

```java
int getArgumentCount()
```

Returns the number of arguments, this option will consume.

**Returns:** number of consumed arguments

- getDescription

```java
String
getDescription()
```

Returns the description of the option. For instance, the option "group", would
return the synopsis of the option such as, "groups the documents".

**Returns:** description if set, otherwise an empty String

- getKind

```java
Doclet.Option.Kind
getKind()
```

Returns the option kind.

**Returns:** the kind of this option

- getNames

```java
List
<
String
> getNames()
```

Returns the list of names that may be used to identify the option. For instance, the
list could be

["-classpath", "--class-path"]

for the
option "-classpath", with an alias "--class-path".

**Returns:** the names of the option

- getParameters

```java
String
getParameters()
```

Returns the parameters of the option. For instance "name <p1>:<p2>.."

**Returns:** parameters if set, otherwise an empty String

- process

```java
boolean process​(
String
option,

List
<
String
> arguments)
```

Processes the option and arguments as needed. This method will
be invoked if the given option name matches the option.

**Parameters:** option

- the option
**Parameters:** arguments

- a list encapsulating the arguments
**Returns:** true if operation succeeded, false otherwise

Method Detail

- getArgumentCount

```java
int getArgumentCount()
```

Returns the number of arguments, this option will consume.

**Returns:** number of consumed arguments

- getDescription

```java
String
getDescription()
```

Returns the description of the option. For instance, the option "group", would
return the synopsis of the option such as, "groups the documents".

**Returns:** description if set, otherwise an empty String

- getKind

```java
Doclet.Option.Kind
getKind()
```

Returns the option kind.

**Returns:** the kind of this option

- getNames

```java
List
<
String
> getNames()
```

Returns the list of names that may be used to identify the option. For instance, the
list could be

["-classpath", "--class-path"]

for the
option "-classpath", with an alias "--class-path".

**Returns:** the names of the option

- getParameters

```java
String
getParameters()
```

Returns the parameters of the option. For instance "name <p1>:<p2>.."

**Returns:** parameters if set, otherwise an empty String

- process

```java
boolean process​(
String
option,

List
<
String
> arguments)
```

Processes the option and arguments as needed. This method will
be invoked if the given option name matches the option.

**Parameters:** option

- the option
**Parameters:** arguments

- a list encapsulating the arguments
**Returns:** true if operation succeeded, false otherwise

---

#### Method Detail

getArgumentCount

```java
int getArgumentCount()
```

Returns the number of arguments, this option will consume.

**Returns:** number of consumed arguments

---

#### getArgumentCount

int getArgumentCount()

Returns the number of arguments, this option will consume.

getDescription

```java
String
getDescription()
```

Returns the description of the option. For instance, the option "group", would
return the synopsis of the option such as, "groups the documents".

**Returns:** description if set, otherwise an empty String

---

#### getDescription

String

getDescription()

Returns the description of the option. For instance, the option "group", would
return the synopsis of the option such as, "groups the documents".

getKind

```java
Doclet.Option.Kind
getKind()
```

Returns the option kind.

**Returns:** the kind of this option

---

#### getKind

Doclet.Option.Kind

getKind()

Returns the option kind.

getNames

```java
List
<
String
> getNames()
```

Returns the list of names that may be used to identify the option. For instance, the
list could be

["-classpath", "--class-path"]

for the
option "-classpath", with an alias "--class-path".

**Returns:** the names of the option

---

#### getNames

List

<

String

> getNames()

Returns the list of names that may be used to identify the option. For instance, the
list could be

["-classpath", "--class-path"]

for the
option "-classpath", with an alias "--class-path".

getParameters

```java
String
getParameters()
```

Returns the parameters of the option. For instance "name <p1>:<p2>.."

**Returns:** parameters if set, otherwise an empty String

---

#### getParameters

String

getParameters()

Returns the parameters of the option. For instance "name <p1>:<p2>.."

process

```java
boolean process​(
String
option,

List
<
String
> arguments)
```

Processes the option and arguments as needed. This method will
be invoked if the given option name matches the option.

**Parameters:** option

- the option
**Parameters:** arguments

- a list encapsulating the arguments
**Returns:** true if operation succeeded, false otherwise

---

#### process

boolean process​(

String

option,

List

<

String

> arguments)

Processes the option and arguments as needed. This method will
be invoked if the given option name matches the option.

---

