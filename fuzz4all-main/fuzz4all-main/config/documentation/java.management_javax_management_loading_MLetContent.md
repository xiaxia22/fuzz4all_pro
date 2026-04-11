# Class MLetContent

**Source:** `java.management\javax\management\loading\MLetContent.html`

### Class Description

```java
public class
MLetContent

extends
Object
```

This class represents the contents of the

MLET

tag.
It can be consulted by a subclass of

MLet

that overrides
the

MLet.check

method.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public MLetContent​(
URL
url,

Map
<
String
,​
String
> attributes,

List
<
String
> types,

List
<
String
> values)

Creates an

MLet

instance initialized with attributes read
from an

MLET

tag in an MLet text file.

**Parameters:**
- url

- The URL of the MLet text file containing the

MLET

tag.
- attributes

- A map of the attributes of the

MLET

tag.
The keys in this map are the attribute names in lowercase, for
example

codebase

. The values are the associated attribute
values.
- types

- A list of the TYPE attributes that appeared in nested
<PARAM> tags.
- values

- A list of the VALUE attributes that appeared in nested
<PARAM> tags.

---

### Method Details

#### public
Map
<
String
,​
String
> getAttributes()

Gets the attributes of the

MLET

tag. The keys in
the returned map are the attribute names in lowercase, for
example

codebase

. The values are the associated
attribute values.

**Returns:**
- A map of the attributes of the

MLET

tag
and their values.

---

#### public
URL
getDocumentBase()

Gets the MLet text file's base URL.

**Returns:**
- The MLet text file's base URL.

---

#### public
URL
getCodeBase()

Gets the code base URL.

**Returns:**
- The code base URL.

---

#### public
String
getJarFiles()

Gets the list of

.jar

files specified by the

ARCHIVE

attribute of the

MLET

tag.

**Returns:**
- A comma-separated list of

.jar

file names.

---

#### public
String
getCode()

Gets the value of the

CODE

attribute of the

MLET

tag.

**Returns:**
- The value of the

CODE

attribute of the

MLET

tag.

---

#### public
String
getSerializedObject()

Gets the value of the

OBJECT

attribute of the

MLET

tag.

**Returns:**
- The value of the

OBJECT

attribute of the

MLET

tag.

---

#### public
String
getName()

Gets the value of the

NAME

attribute of the

MLET

tag.

**Returns:**
- The value of the

NAME

attribute of the

MLET

tag.

---

#### public
String
getVersion()

Gets the value of the

VERSION

attribute of the

MLET

tag.

**Returns:**
- The value of the

VERSION

attribute of the

MLET

tag.

---

#### public
List
<
String
> getParameterTypes()

Gets the list of values of the

TYPE

attribute in
each nested <PARAM> tag within the

MLET

tag.

**Returns:**
- the list of types.

---

#### public
List
<
String
> getParameterValues()

Gets the list of values of the

VALUE

attribute in
each nested <PARAM> tag within the

MLET

tag.

**Returns:**
- the list of values.

---

### Additional Sections

#### Class MLetContent

java.lang.Object

- javax.management.loading.MLetContent

javax.management.loading.MLetContent

```java
public class
MLetContent

extends
Object
```

This class represents the contents of the

MLET

tag.
It can be consulted by a subclass of

MLet

that overrides
the

MLet.check

method.

**Since:** 1.6

public class

MLetContent

extends

Object

This class represents the contents of the

MLET

tag.
It can be consulted by a subclass of

MLet

that overrides
the

MLet.check

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MLetContent

​(

URL

url,

Map

<

String

,​

String

> attributes,

List

<

String

> types,

List

<

String

> values)

Creates an

MLet

instance initialized with attributes read
from an

MLET

tag in an MLet text file.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Map

<

String

,​

String

>

getAttributes

()

Gets the attributes of the

MLET

tag.

String

getCode

()

Gets the value of the

CODE

attribute of the

MLET

tag.

URL

getCodeBase

()

Gets the code base URL.

URL

getDocumentBase

()

Gets the MLet text file's base URL.

String

getJarFiles

()

Gets the list of

.jar

files specified by the

ARCHIVE

attribute of the

MLET

tag.

String

getName

()

Gets the value of the

NAME

attribute of the

MLET

tag.

List

<

String

>

getParameterTypes

()

Gets the list of values of the

TYPE

attribute in
each nested <PARAM> tag within the

MLET

tag.

List

<

String

>

getParameterValues

()

Gets the list of values of the

VALUE

attribute in
each nested <PARAM> tag within the

MLET

tag.

String

getSerializedObject

()

Gets the value of the

OBJECT

attribute of the

MLET

tag.

String

getVersion

()

Gets the value of the

VERSION

attribute of the

MLET

tag.

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

MLetContent

​(

URL

url,

Map

<

String

,​

String

> attributes,

List

<

String

> types,

List

<

String

> values)

Creates an

MLet

instance initialized with attributes read
from an

MLET

tag in an MLet text file.

---

#### Constructor Summary

Creates an

MLet

instance initialized with attributes read
from an

MLET

tag in an MLet text file.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Map

<

String

,​

String

>

getAttributes

()

Gets the attributes of the

MLET

tag.

String

getCode

()

Gets the value of the

CODE

attribute of the

MLET

tag.

URL

getCodeBase

()

Gets the code base URL.

URL

getDocumentBase

()

Gets the MLet text file's base URL.

String

getJarFiles

()

Gets the list of

.jar

files specified by the

ARCHIVE

attribute of the

MLET

tag.

String

getName

()

Gets the value of the

NAME

attribute of the

MLET

tag.

List

<

String

>

getParameterTypes

()

Gets the list of values of the

TYPE

attribute in
each nested <PARAM> tag within the

MLET

tag.

List

<

String

>

getParameterValues

()

Gets the list of values of the

VALUE

attribute in
each nested <PARAM> tag within the

MLET

tag.

String

getSerializedObject

()

Gets the value of the

OBJECT

attribute of the

MLET

tag.

String

getVersion

()

Gets the value of the

VERSION

attribute of the

MLET

tag.

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

Gets the attributes of the

MLET

tag.

Gets the value of the

CODE

attribute of the

MLET

tag.

Gets the code base URL.

Gets the MLet text file's base URL.

Gets the list of

.jar

files specified by the

ARCHIVE

attribute of the

MLET

tag.

Gets the value of the

NAME

attribute of the

MLET

tag.

Gets the list of values of the

TYPE

attribute in
each nested <PARAM> tag within the

MLET

tag.

Gets the list of values of the

VALUE

attribute in
each nested <PARAM> tag within the

MLET

tag.

Gets the value of the

OBJECT

attribute of the

MLET

tag.

Gets the value of the

VERSION

attribute of the

MLET

tag.

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

- MLetContent

```java
public MLetContent​(
URL
url,

Map
<
String
,​
String
> attributes,

List
<
String
> types,

List
<
String
> values)
```

Creates an

MLet

instance initialized with attributes read
from an

MLET

tag in an MLet text file.

**Parameters:** url

- The URL of the MLet text file containing the

MLET

tag.
**Parameters:** attributes

- A map of the attributes of the

MLET

tag.
The keys in this map are the attribute names in lowercase, for
example

codebase

. The values are the associated attribute
values.
**Parameters:** types

- A list of the TYPE attributes that appeared in nested
<PARAM> tags.
**Parameters:** values

- A list of the VALUE attributes that appeared in nested
<PARAM> tags.

============ METHOD DETAIL ==========

- Method Detail

- getAttributes

```java
public
Map
<
String
,​
String
> getAttributes()
```

Gets the attributes of the

MLET

tag. The keys in
the returned map are the attribute names in lowercase, for
example

codebase

. The values are the associated
attribute values.

**Returns:** A map of the attributes of the

MLET

tag
and their values.

- getDocumentBase

```java
public
URL
getDocumentBase()
```

Gets the MLet text file's base URL.

**Returns:** The MLet text file's base URL.

- getCodeBase

```java
public
URL
getCodeBase()
```

Gets the code base URL.

**Returns:** The code base URL.

- getJarFiles

```java
public
String
getJarFiles()
```

Gets the list of

.jar

files specified by the

ARCHIVE

attribute of the

MLET

tag.

**Returns:** A comma-separated list of

.jar

file names.

- getCode

```java
public
String
getCode()
```

Gets the value of the

CODE

attribute of the

MLET

tag.

**Returns:** The value of the

CODE

attribute of the

MLET

tag.

- getSerializedObject

```java
public
String
getSerializedObject()
```

Gets the value of the

OBJECT

attribute of the

MLET

tag.

**Returns:** The value of the

OBJECT

attribute of the

MLET

tag.

- getName

```java
public
String
getName()
```

Gets the value of the

NAME

attribute of the

MLET

tag.

**Returns:** The value of the

NAME

attribute of the

MLET

tag.

- getVersion

```java
public
String
getVersion()
```

Gets the value of the

VERSION

attribute of the

MLET

tag.

**Returns:** The value of the

VERSION

attribute of the

MLET

tag.

- getParameterTypes

```java
public
List
<
String
> getParameterTypes()
```

Gets the list of values of the

TYPE

attribute in
each nested <PARAM> tag within the

MLET

tag.

**Returns:** the list of types.

- getParameterValues

```java
public
List
<
String
> getParameterValues()
```

Gets the list of values of the

VALUE

attribute in
each nested <PARAM> tag within the

MLET

tag.

**Returns:** the list of values.

Constructor Detail

- MLetContent

```java
public MLetContent​(
URL
url,

Map
<
String
,​
String
> attributes,

List
<
String
> types,

List
<
String
> values)
```

Creates an

MLet

instance initialized with attributes read
from an

MLET

tag in an MLet text file.

**Parameters:** url

- The URL of the MLet text file containing the

MLET

tag.
**Parameters:** attributes

- A map of the attributes of the

MLET

tag.
The keys in this map are the attribute names in lowercase, for
example

codebase

. The values are the associated attribute
values.
**Parameters:** types

- A list of the TYPE attributes that appeared in nested
<PARAM> tags.
**Parameters:** values

- A list of the VALUE attributes that appeared in nested
<PARAM> tags.

---

#### Constructor Detail

MLetContent

```java
public MLetContent​(
URL
url,

Map
<
String
,​
String
> attributes,

List
<
String
> types,

List
<
String
> values)
```

Creates an

MLet

instance initialized with attributes read
from an

MLET

tag in an MLet text file.

**Parameters:** url

- The URL of the MLet text file containing the

MLET

tag.
**Parameters:** attributes

- A map of the attributes of the

MLET

tag.
The keys in this map are the attribute names in lowercase, for
example

codebase

. The values are the associated attribute
values.
**Parameters:** types

- A list of the TYPE attributes that appeared in nested
<PARAM> tags.
**Parameters:** values

- A list of the VALUE attributes that appeared in nested
<PARAM> tags.

---

#### MLetContent

public MLetContent​(

URL

url,

Map

<

String

,​

String

> attributes,

List

<

String

> types,

List

<

String

> values)

Creates an

MLet

instance initialized with attributes read
from an

MLET

tag in an MLet text file.

Method Detail

- getAttributes

```java
public
Map
<
String
,​
String
> getAttributes()
```

Gets the attributes of the

MLET

tag. The keys in
the returned map are the attribute names in lowercase, for
example

codebase

. The values are the associated
attribute values.

**Returns:** A map of the attributes of the

MLET

tag
and their values.

- getDocumentBase

```java
public
URL
getDocumentBase()
```

Gets the MLet text file's base URL.

**Returns:** The MLet text file's base URL.

- getCodeBase

```java
public
URL
getCodeBase()
```

Gets the code base URL.

**Returns:** The code base URL.

- getJarFiles

```java
public
String
getJarFiles()
```

Gets the list of

.jar

files specified by the

ARCHIVE

attribute of the

MLET

tag.

**Returns:** A comma-separated list of

.jar

file names.

- getCode

```java
public
String
getCode()
```

Gets the value of the

CODE

attribute of the

MLET

tag.

**Returns:** The value of the

CODE

attribute of the

MLET

tag.

- getSerializedObject

```java
public
String
getSerializedObject()
```

Gets the value of the

OBJECT

attribute of the

MLET

tag.

**Returns:** The value of the

OBJECT

attribute of the

MLET

tag.

- getName

```java
public
String
getName()
```

Gets the value of the

NAME

attribute of the

MLET

tag.

**Returns:** The value of the

NAME

attribute of the

MLET

tag.

- getVersion

```java
public
String
getVersion()
```

Gets the value of the

VERSION

attribute of the

MLET

tag.

**Returns:** The value of the

VERSION

attribute of the

MLET

tag.

- getParameterTypes

```java
public
List
<
String
> getParameterTypes()
```

Gets the list of values of the

TYPE

attribute in
each nested <PARAM> tag within the

MLET

tag.

**Returns:** the list of types.

- getParameterValues

```java
public
List
<
String
> getParameterValues()
```

Gets the list of values of the

VALUE

attribute in
each nested <PARAM> tag within the

MLET

tag.

**Returns:** the list of values.

---

#### Method Detail

getAttributes

```java
public
Map
<
String
,​
String
> getAttributes()
```

Gets the attributes of the

MLET

tag. The keys in
the returned map are the attribute names in lowercase, for
example

codebase

. The values are the associated
attribute values.

**Returns:** A map of the attributes of the

MLET

tag
and their values.

---

#### getAttributes

public

Map

<

String

,​

String

> getAttributes()

Gets the attributes of the

MLET

tag. The keys in
the returned map are the attribute names in lowercase, for
example

codebase

. The values are the associated
attribute values.

getDocumentBase

```java
public
URL
getDocumentBase()
```

Gets the MLet text file's base URL.

**Returns:** The MLet text file's base URL.

---

#### getDocumentBase

public

URL

getDocumentBase()

Gets the MLet text file's base URL.

getCodeBase

```java
public
URL
getCodeBase()
```

Gets the code base URL.

**Returns:** The code base URL.

---

#### getCodeBase

public

URL

getCodeBase()

Gets the code base URL.

getJarFiles

```java
public
String
getJarFiles()
```

Gets the list of

.jar

files specified by the

ARCHIVE

attribute of the

MLET

tag.

**Returns:** A comma-separated list of

.jar

file names.

---

#### getJarFiles

public

String

getJarFiles()

Gets the list of

.jar

files specified by the

ARCHIVE

attribute of the

MLET

tag.

getCode

```java
public
String
getCode()
```

Gets the value of the

CODE

attribute of the

MLET

tag.

**Returns:** The value of the

CODE

attribute of the

MLET

tag.

---

#### getCode

public

String

getCode()

Gets the value of the

CODE

attribute of the

MLET

tag.

getSerializedObject

```java
public
String
getSerializedObject()
```

Gets the value of the

OBJECT

attribute of the

MLET

tag.

**Returns:** The value of the

OBJECT

attribute of the

MLET

tag.

---

#### getSerializedObject

public

String

getSerializedObject()

Gets the value of the

OBJECT

attribute of the

MLET

tag.

getName

```java
public
String
getName()
```

Gets the value of the

NAME

attribute of the

MLET

tag.

**Returns:** The value of the

NAME

attribute of the

MLET

tag.

---

#### getName

public

String

getName()

Gets the value of the

NAME

attribute of the

MLET

tag.

getVersion

```java
public
String
getVersion()
```

Gets the value of the

VERSION

attribute of the

MLET

tag.

**Returns:** The value of the

VERSION

attribute of the

MLET

tag.

---

#### getVersion

public

String

getVersion()

Gets the value of the

VERSION

attribute of the

MLET

tag.

getParameterTypes

```java
public
List
<
String
> getParameterTypes()
```

Gets the list of values of the

TYPE

attribute in
each nested <PARAM> tag within the

MLET

tag.

**Returns:** the list of types.

---

#### getParameterTypes

public

List

<

String

> getParameterTypes()

Gets the list of values of the

TYPE

attribute in
each nested <PARAM> tag within the

MLET

tag.

getParameterValues

```java
public
List
<
String
> getParameterValues()
```

Gets the list of values of the

VALUE

attribute in
each nested <PARAM> tag within the

MLET

tag.

**Returns:** the list of values.

---

#### getParameterValues

public

List

<

String

> getParameterValues()

Gets the list of values of the

VALUE

attribute in
each nested <PARAM> tag within the

MLET

tag.

---

