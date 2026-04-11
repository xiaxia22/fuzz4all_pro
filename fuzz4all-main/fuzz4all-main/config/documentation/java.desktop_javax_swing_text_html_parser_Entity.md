# Class Entity

**Source:** `java.desktop\javax\swing\text\html\parser\Entity.html`

### Class Description

```java
public final class
Entity

extends
Object

implements
DTDConstants
```

An entity is described in a DTD using the ENTITY construct.
It defines the type and value of the entity.

**All Implemented Interfaces:** DTDConstants

---

### Field Details

#### public
String
name

The name of the entity.

---

#### public int type

The type of the entity.

---

#### public char[] data

The char array of data.

---

### Constructor Details

#### public Entity​(
String
name,
int type,
char[] data)

Creates an entity.

**Parameters:**
- name

- the name of the entity
- type

- the type of the entity
- data

- the char array of data

---

### Method Details

#### public
String
getName()

Gets the name of the entity.

**Returns:**
- the name of the entity, as a

String

---

#### public int getType()

Gets the type of the entity.

**Returns:**
- the type of the entity

---

#### public boolean isParameter()

Returns

true

if it is a parameter entity.

**Returns:**
- true

if it is a parameter entity

---

#### public boolean isGeneral()

Returns

true

if it is a general entity.

**Returns:**
- true

if it is a general entity

---

#### public char[] getData()

Returns the

data

.

**Returns:**
- the

data

---

#### public
String
getString()

Returns the data as a

String

.

**Returns:**
- the data as a

String

---

#### public static int name2type​(
String
nm)

Converts

nm

string to the corresponding
entity type. If the string does not have a corresponding
entity type, returns the type corresponding to "CDATA".
Valid entity types are: "PUBLIC", "CDATA", "SDATA", "PI",
"STARTTAG", "ENDTAG", "MS", "MD", "SYSTEM".

**Parameters:**
- nm

- the string to be converted

**Returns:**
- the corresponding entity type, or the type corresponding
to "CDATA", if none exists

---

### Additional Sections

#### Class Entity

java.lang.Object

- javax.swing.text.html.parser.Entity

javax.swing.text.html.parser.Entity

**All Implemented Interfaces:** DTDConstants

```java
public final class
Entity

extends
Object

implements
DTDConstants
```

An entity is described in a DTD using the ENTITY construct.
It defines the type and value of the entity.

**See Also:** DTD

public final class

Entity

extends

Object

implements

DTDConstants

An entity is described in a DTD using the ENTITY construct.
It defines the type and value of the entity.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

char[]

data

The char array of data.

String

name

The name of the entity.

int

type

The type of the entity.

- Fields declared in interface javax.swing.text.html.parser.

DTDConstants

ANY

,

CDATA

,

CONREF

,

CURRENT

,

DEFAULT

,

EMPTY

,

ENDTAG

,

ENTITIES

,

ENTITY

,

FIXED

,

GENERAL

,

ID

,

IDREF

,

IDREFS

,

IMPLIED

,

MD

,

MODEL

,

MS

,

NAME

,

NAMES

,

NMTOKEN

,

NMTOKENS

,

NOTATION

,

NUMBER

,

NUMBERS

,

NUTOKEN

,

NUTOKENS

,

PARAMETER

,

PI

,

PUBLIC

,

RCDATA

,

REQUIRED

,

SDATA

,

STARTTAG

,

SYSTEM

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Entity

​(

String

name,
int type,
char[] data)

Creates an entity.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

char[]

getData

()

Returns the

data

.

String

getName

()

Gets the name of the entity.

String

getString

()

Returns the data as a

String

.

int

getType

()

Gets the type of the entity.

boolean

isGeneral

()

Returns

true

if it is a general entity.

boolean

isParameter

()

Returns

true

if it is a parameter entity.

static int

name2type

​(

String

nm)

Converts

nm

string to the corresponding
entity type.

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

char[]

data

The char array of data.

String

name

The name of the entity.

int

type

The type of the entity.

- Fields declared in interface javax.swing.text.html.parser.

DTDConstants

ANY

,

CDATA

,

CONREF

,

CURRENT

,

DEFAULT

,

EMPTY

,

ENDTAG

,

ENTITIES

,

ENTITY

,

FIXED

,

GENERAL

,

ID

,

IDREF

,

IDREFS

,

IMPLIED

,

MD

,

MODEL

,

MS

,

NAME

,

NAMES

,

NMTOKEN

,

NMTOKENS

,

NOTATION

,

NUMBER

,

NUMBERS

,

NUTOKEN

,

NUTOKENS

,

PARAMETER

,

PI

,

PUBLIC

,

RCDATA

,

REQUIRED

,

SDATA

,

STARTTAG

,

SYSTEM

---

#### Field Summary

The char array of data.

The name of the entity.

The type of the entity.

Fields declared in interface javax.swing.text.html.parser.

DTDConstants

ANY

,

CDATA

,

CONREF

,

CURRENT

,

DEFAULT

,

EMPTY

,

ENDTAG

,

ENTITIES

,

ENTITY

,

FIXED

,

GENERAL

,

ID

,

IDREF

,

IDREFS

,

IMPLIED

,

MD

,

MODEL

,

MS

,

NAME

,

NAMES

,

NMTOKEN

,

NMTOKENS

,

NOTATION

,

NUMBER

,

NUMBERS

,

NUTOKEN

,

NUTOKENS

,

PARAMETER

,

PI

,

PUBLIC

,

RCDATA

,

REQUIRED

,

SDATA

,

STARTTAG

,

SYSTEM

---

#### Fields declared in interface javax.swing.text.html.parser. DTDConstants

Constructor Summary

Constructors

Constructor

Description

Entity

​(

String

name,
int type,
char[] data)

Creates an entity.

---

#### Constructor Summary

Creates an entity.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

char[]

getData

()

Returns the

data

.

String

getName

()

Gets the name of the entity.

String

getString

()

Returns the data as a

String

.

int

getType

()

Gets the type of the entity.

boolean

isGeneral

()

Returns

true

if it is a general entity.

boolean

isParameter

()

Returns

true

if it is a parameter entity.

static int

name2type

​(

String

nm)

Converts

nm

string to the corresponding
entity type.

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

Returns the

data

.

Gets the name of the entity.

Returns the data as a

String

.

Gets the type of the entity.

Returns

true

if it is a general entity.

Returns

true

if it is a parameter entity.

Converts

nm

string to the corresponding
entity type.

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

- name

```java
public
String
name
```

The name of the entity.

- type

```java
public int type
```

The type of the entity.

- data

```java
public char[] data
```

The char array of data.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Entity

```java
public Entity​(
String
name,
int type,
char[] data)
```

Creates an entity.

**Parameters:** name

- the name of the entity
**Parameters:** type

- the type of the entity
**Parameters:** data

- the char array of data

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Gets the name of the entity.

**Returns:** the name of the entity, as a

String

- getType

```java
public int getType()
```

Gets the type of the entity.

**Returns:** the type of the entity

- isParameter

```java
public boolean isParameter()
```

Returns

true

if it is a parameter entity.

**Returns:** true

if it is a parameter entity

- isGeneral

```java
public boolean isGeneral()
```

Returns

true

if it is a general entity.

**Returns:** true

if it is a general entity

- getData

```java
public char[] getData()
```

Returns the

data

.

**Returns:** the

data

- getString

```java
public
String
getString()
```

Returns the data as a

String

.

**Returns:** the data as a

String

- name2type

```java
public static int name2type​(
String
nm)
```

Converts

nm

string to the corresponding
entity type. If the string does not have a corresponding
entity type, returns the type corresponding to "CDATA".
Valid entity types are: "PUBLIC", "CDATA", "SDATA", "PI",
"STARTTAG", "ENDTAG", "MS", "MD", "SYSTEM".

**Parameters:** nm

- the string to be converted
**Returns:** the corresponding entity type, or the type corresponding
to "CDATA", if none exists

Field Detail

- name

```java
public
String
name
```

The name of the entity.

- type

```java
public int type
```

The type of the entity.

- data

```java
public char[] data
```

The char array of data.

---

#### Field Detail

name

```java
public
String
name
```

The name of the entity.

---

#### name

public

String

name

The name of the entity.

type

```java
public int type
```

The type of the entity.

---

#### type

public int type

The type of the entity.

data

```java
public char[] data
```

The char array of data.

---

#### data

public char[] data

The char array of data.

Constructor Detail

- Entity

```java
public Entity​(
String
name,
int type,
char[] data)
```

Creates an entity.

**Parameters:** name

- the name of the entity
**Parameters:** type

- the type of the entity
**Parameters:** data

- the char array of data

---

#### Constructor Detail

Entity

```java
public Entity​(
String
name,
int type,
char[] data)
```

Creates an entity.

**Parameters:** name

- the name of the entity
**Parameters:** type

- the type of the entity
**Parameters:** data

- the char array of data

---

#### Entity

public Entity​(

String

name,
int type,
char[] data)

Creates an entity.

Method Detail

- getName

```java
public
String
getName()
```

Gets the name of the entity.

**Returns:** the name of the entity, as a

String

- getType

```java
public int getType()
```

Gets the type of the entity.

**Returns:** the type of the entity

- isParameter

```java
public boolean isParameter()
```

Returns

true

if it is a parameter entity.

**Returns:** true

if it is a parameter entity

- isGeneral

```java
public boolean isGeneral()
```

Returns

true

if it is a general entity.

**Returns:** true

if it is a general entity

- getData

```java
public char[] getData()
```

Returns the

data

.

**Returns:** the

data

- getString

```java
public
String
getString()
```

Returns the data as a

String

.

**Returns:** the data as a

String

- name2type

```java
public static int name2type​(
String
nm)
```

Converts

nm

string to the corresponding
entity type. If the string does not have a corresponding
entity type, returns the type corresponding to "CDATA".
Valid entity types are: "PUBLIC", "CDATA", "SDATA", "PI",
"STARTTAG", "ENDTAG", "MS", "MD", "SYSTEM".

**Parameters:** nm

- the string to be converted
**Returns:** the corresponding entity type, or the type corresponding
to "CDATA", if none exists

---

#### Method Detail

getName

```java
public
String
getName()
```

Gets the name of the entity.

**Returns:** the name of the entity, as a

String

---

#### getName

public

String

getName()

Gets the name of the entity.

getType

```java
public int getType()
```

Gets the type of the entity.

**Returns:** the type of the entity

---

#### getType

public int getType()

Gets the type of the entity.

isParameter

```java
public boolean isParameter()
```

Returns

true

if it is a parameter entity.

**Returns:** true

if it is a parameter entity

---

#### isParameter

public boolean isParameter()

Returns

true

if it is a parameter entity.

isGeneral

```java
public boolean isGeneral()
```

Returns

true

if it is a general entity.

**Returns:** true

if it is a general entity

---

#### isGeneral

public boolean isGeneral()

Returns

true

if it is a general entity.

getData

```java
public char[] getData()
```

Returns the

data

.

**Returns:** the

data

---

#### getData

public char[] getData()

Returns the

data

.

getString

```java
public
String
getString()
```

Returns the data as a

String

.

**Returns:** the data as a

String

---

#### getString

public

String

getString()

Returns the data as a

String

.

name2type

```java
public static int name2type​(
String
nm)
```

Converts

nm

string to the corresponding
entity type. If the string does not have a corresponding
entity type, returns the type corresponding to "CDATA".
Valid entity types are: "PUBLIC", "CDATA", "SDATA", "PI",
"STARTTAG", "ENDTAG", "MS", "MD", "SYSTEM".

**Parameters:** nm

- the string to be converted
**Returns:** the corresponding entity type, or the type corresponding
to "CDATA", if none exists

---

#### name2type

public static int name2type​(

String

nm)

Converts

nm

string to the corresponding
entity type. If the string does not have a corresponding
entity type, returns the type corresponding to "CDATA".
Valid entity types are: "PUBLIC", "CDATA", "SDATA", "PI",
"STARTTAG", "ENDTAG", "MS", "MD", "SYSTEM".

---

