# Class DriverPropertyInfo

**Source:** `java.sql\java\sql\DriverPropertyInfo.html`

### Class Description

```java
public class
DriverPropertyInfo

extends
Object
```

Driver properties for making a connection. The

DriverPropertyInfo

class is of interest only to advanced programmers
who need to interact with a Driver via the method

getDriverProperties

to discover
and supply properties for connections.

**Since:** 1.1

---

### Field Details

#### public
String
name

The name of the property.

---

#### public
String
description

A brief description of the property, which may be null.

---

#### public boolean required

The

required

field is

true

if a value must be
supplied for this property
during

Driver.connect

and

false

otherwise.

---

#### public
String
value

The

value

field specifies the current value of
the property, based on a combination of the information
supplied to the method

getPropertyInfo

, the
Java environment, and the driver-supplied default values. This field
may be null if no value is known.

---

#### public
String
[] choices

An array of possible values if the value for the field

DriverPropertyInfo.value

may be selected
from a particular set of values; otherwise null.

---

### Constructor Details

#### public DriverPropertyInfo​(
String
name,

String
value)

Constructs a

DriverPropertyInfo

object with a given
name and value. The

description

and

choices

are initialized to

null

and

required

is initialized
to

false

.

**Parameters:**
- name

- the name of the property
- value

- the current value, which may be null

---

### Method Details

*No entries found.*

### Additional Sections

#### Class DriverPropertyInfo

java.lang.Object

- java.sql.DriverPropertyInfo

java.sql.DriverPropertyInfo

```java
public class
DriverPropertyInfo

extends
Object
```

Driver properties for making a connection. The

DriverPropertyInfo

class is of interest only to advanced programmers
who need to interact with a Driver via the method

getDriverProperties

to discover
and supply properties for connections.

**Since:** 1.1

public class

DriverPropertyInfo

extends

Object

Driver properties for making a connection. The

DriverPropertyInfo

class is of interest only to advanced programmers
who need to interact with a Driver via the method

getDriverProperties

to discover
and supply properties for connections.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

String

[]

choices

An array of possible values if the value for the field

DriverPropertyInfo.value

may be selected
from a particular set of values; otherwise null.

String

description

A brief description of the property, which may be null.

String

name

The name of the property.

boolean

required

The

required

field is

true

if a value must be
supplied for this property
during

Driver.connect

and

false

otherwise.

String

value

The

value

field specifies the current value of
the property, based on a combination of the information
supplied to the method

getPropertyInfo

, the
Java environment, and the driver-supplied default values.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DriverPropertyInfo

​(

String

name,

String

value)

Constructs a

DriverPropertyInfo

object with a given
name and value.

========== METHOD SUMMARY ===========

- Method Summary

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

String

[]

choices

An array of possible values if the value for the field

DriverPropertyInfo.value

may be selected
from a particular set of values; otherwise null.

String

description

A brief description of the property, which may be null.

String

name

The name of the property.

boolean

required

The

required

field is

true

if a value must be
supplied for this property
during

Driver.connect

and

false

otherwise.

String

value

The

value

field specifies the current value of
the property, based on a combination of the information
supplied to the method

getPropertyInfo

, the
Java environment, and the driver-supplied default values.

---

#### Field Summary

An array of possible values if the value for the field

DriverPropertyInfo.value

may be selected
from a particular set of values; otherwise null.

A brief description of the property, which may be null.

The name of the property.

The

required

field is

true

if a value must be
supplied for this property
during

Driver.connect

and

false

otherwise.

The

value

field specifies the current value of
the property, based on a combination of the information
supplied to the method

getPropertyInfo

, the
Java environment, and the driver-supplied default values.

Constructor Summary

Constructors

Constructor

Description

DriverPropertyInfo

​(

String

name,

String

value)

Constructs a

DriverPropertyInfo

object with a given
name and value.

---

#### Constructor Summary

Constructs a

DriverPropertyInfo

object with a given
name and value.

Method Summary

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

The name of the property.

- description

```java
public
String
description
```

A brief description of the property, which may be null.

- required

```java
public boolean required
```

The

required

field is

true

if a value must be
supplied for this property
during

Driver.connect

and

false

otherwise.

- value

```java
public
String
value
```

The

value

field specifies the current value of
the property, based on a combination of the information
supplied to the method

getPropertyInfo

, the
Java environment, and the driver-supplied default values. This field
may be null if no value is known.

- choices

```java
public
String
[] choices
```

An array of possible values if the value for the field

DriverPropertyInfo.value

may be selected
from a particular set of values; otherwise null.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DriverPropertyInfo

```java
public DriverPropertyInfo​(
String
name,

String
value)
```

Constructs a

DriverPropertyInfo

object with a given
name and value. The

description

and

choices

are initialized to

null

and

required

is initialized
to

false

.

**Parameters:** name

- the name of the property
**Parameters:** value

- the current value, which may be null

Field Detail

- name

```java
public
String
name
```

The name of the property.

- description

```java
public
String
description
```

A brief description of the property, which may be null.

- required

```java
public boolean required
```

The

required

field is

true

if a value must be
supplied for this property
during

Driver.connect

and

false

otherwise.

- value

```java
public
String
value
```

The

value

field specifies the current value of
the property, based on a combination of the information
supplied to the method

getPropertyInfo

, the
Java environment, and the driver-supplied default values. This field
may be null if no value is known.

- choices

```java
public
String
[] choices
```

An array of possible values if the value for the field

DriverPropertyInfo.value

may be selected
from a particular set of values; otherwise null.

---

#### Field Detail

name

```java
public
String
name
```

The name of the property.

---

#### name

public

String

name

The name of the property.

description

```java
public
String
description
```

A brief description of the property, which may be null.

---

#### description

public

String

description

A brief description of the property, which may be null.

required

```java
public boolean required
```

The

required

field is

true

if a value must be
supplied for this property
during

Driver.connect

and

false

otherwise.

---

#### required

public boolean required

The

required

field is

true

if a value must be
supplied for this property
during

Driver.connect

and

false

otherwise.

value

```java
public
String
value
```

The

value

field specifies the current value of
the property, based on a combination of the information
supplied to the method

getPropertyInfo

, the
Java environment, and the driver-supplied default values. This field
may be null if no value is known.

---

#### value

public

String

value

The

value

field specifies the current value of
the property, based on a combination of the information
supplied to the method

getPropertyInfo

, the
Java environment, and the driver-supplied default values. This field
may be null if no value is known.

choices

```java
public
String
[] choices
```

An array of possible values if the value for the field

DriverPropertyInfo.value

may be selected
from a particular set of values; otherwise null.

---

#### choices

public

String

[] choices

An array of possible values if the value for the field

DriverPropertyInfo.value

may be selected
from a particular set of values; otherwise null.

Constructor Detail

- DriverPropertyInfo

```java
public DriverPropertyInfo​(
String
name,

String
value)
```

Constructs a

DriverPropertyInfo

object with a given
name and value. The

description

and

choices

are initialized to

null

and

required

is initialized
to

false

.

**Parameters:** name

- the name of the property
**Parameters:** value

- the current value, which may be null

---

#### Constructor Detail

DriverPropertyInfo

```java
public DriverPropertyInfo​(
String
name,

String
value)
```

Constructs a

DriverPropertyInfo

object with a given
name and value. The

description

and

choices

are initialized to

null

and

required

is initialized
to

false

.

**Parameters:** name

- the name of the property
**Parameters:** value

- the current value, which may be null

---

#### DriverPropertyInfo

public DriverPropertyInfo​(

String

name,

String

value)

Constructs a

DriverPropertyInfo

object with a given
name and value. The

description

and

choices

are initialized to

null

and

required

is initialized
to

false

.

---

