# Class VMOption

**Source:** `jdk.management\com\sun\management\VMOption.html`

### Class Description

```java
public class
VMOption

extends
Object
```

Information about a VM option including its value and
where the value came from which is referred as its

origin

.

Each VM option has a default value. A VM option can
be set at VM creation time typically as a command line
argument to the launcher or an argument passed to the
VM created using the JNI invocation interface.
In addition, a VM option may be set via an environment
variable or a configuration file. A VM option can also
be set dynamically via a management interface after
the VM was started.

A

VMOption

contains the value of a VM option
and the origin of that value at the time this

VMOption

object was constructed. The value of the VM option
may be changed after the

VMOption

object was constructed,

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public VMOption​(
String
name,

String
value,
boolean writeable,

VMOption.Origin
origin)

Constructs a

VMOption

.

**Parameters:**
- name

- Name of a VM option.
- value

- Value of a VM option.
- writeable

-

true

if a VM option can be set dynamically,
or

false

otherwise.
- origin

- where the value of a VM option came from.

**Throws:**
- NullPointerException

- if the name or value is

null

---

### Method Details

#### public
String
getName()

Returns the name of this VM option.

**Returns:**
- the name of this VM option.

---

#### public
String
getValue()

Returns the value of this VM option at the time when
this

VMOption

was created. The value could have been changed.

**Returns:**
- the value of the VM option at the time when
this

VMOption

was created.

---

#### public
VMOption.Origin
getOrigin()

Returns the origin of the value of this VM option. That is,
where the value of this VM option came from.

**Returns:**
- where the value of this VM option came from.

---

#### public boolean isWriteable()

Tests if this VM option is writeable. If this VM option is writeable,
it can be set by the

HotSpotDiagnosticMXBean.setVMOption

method.

**Returns:**
- true

if this VM option is writeable;

false

otherwise.

---

#### public static
VMOption
from​(
CompositeData
cd)

Returns a

VMOption

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

description

Attribute Name

Type

name

java.lang.String

value

java.lang.String

origin

java.lang.String

writeable

java.lang.Boolean

**Parameters:**
- cd

-

CompositeData

representing a

VMOption

**Returns:**
- a

VMOption

object represented by

cd

if

cd

is not

null

;

null

otherwise.

**Throws:**
- IllegalArgumentException

- if

cd

does not
represent a

VMOption

with the attributes described
above.

---

### Additional Sections

#### Class VMOption

java.lang.Object

- com.sun.management.VMOption

com.sun.management.VMOption

```java
public class
VMOption

extends
Object
```

Information about a VM option including its value and
where the value came from which is referred as its

origin

.

Each VM option has a default value. A VM option can
be set at VM creation time typically as a command line
argument to the launcher or an argument passed to the
VM created using the JNI invocation interface.
In addition, a VM option may be set via an environment
variable or a configuration file. A VM option can also
be set dynamically via a management interface after
the VM was started.

A

VMOption

contains the value of a VM option
and the origin of that value at the time this

VMOption

object was constructed. The value of the VM option
may be changed after the

VMOption

object was constructed,

**Since:** 1.6

public class

VMOption

extends

Object

Information about a VM option including its value and
where the value came from which is referred as its

origin

.

Each VM option has a default value. A VM option can
be set at VM creation time typically as a command line
argument to the launcher or an argument passed to the
VM created using the JNI invocation interface.
In addition, a VM option may be set via an environment
variable or a configuration file. A VM option can also
be set dynamically via a management interface after
the VM was started.

A

VMOption

contains the value of a VM option
and the origin of that value at the time this

VMOption

object was constructed. The value of the VM option
may be changed after the

VMOption

object was constructed,

Each VM option has a default value. A VM option can
be set at VM creation time typically as a command line
argument to the launcher or an argument passed to the
VM created using the JNI invocation interface.
In addition, a VM option may be set via an environment
variable or a configuration file. A VM option can also
be set dynamically via a management interface after
the VM was started.

A

VMOption

contains the value of a VM option
and the origin of that value at the time this

VMOption

object was constructed. The value of the VM option
may be changed after the

VMOption

object was constructed,

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

VMOption.Origin

Origin of the value of a VM option.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

VMOption

​(

String

name,

String

value,
boolean writeable,

VMOption.Origin

origin)

Constructs a

VMOption

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

VMOption

from

​(

CompositeData

cd)

Returns a

VMOption

object represented by the
given

CompositeData

.

String

getName

()

Returns the name of this VM option.

VMOption.Origin

getOrigin

()

Returns the origin of the value of this VM option.

String

getValue

()

Returns the value of this VM option at the time when
this

VMOption

was created.

boolean

isWriteable

()

Tests if this VM option is writeable.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

VMOption.Origin

Origin of the value of a VM option.

---

#### Nested Class Summary

Origin of the value of a VM option.

Constructor Summary

Constructors

Constructor

Description

VMOption

​(

String

name,

String

value,
boolean writeable,

VMOption.Origin

origin)

Constructs a

VMOption

.

---

#### Constructor Summary

Constructs a

VMOption

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

VMOption

from

​(

CompositeData

cd)

Returns a

VMOption

object represented by the
given

CompositeData

.

String

getName

()

Returns the name of this VM option.

VMOption.Origin

getOrigin

()

Returns the origin of the value of this VM option.

String

getValue

()

Returns the value of this VM option at the time when
this

VMOption

was created.

boolean

isWriteable

()

Tests if this VM option is writeable.

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

Returns a

VMOption

object represented by the
given

CompositeData

.

Returns the name of this VM option.

Returns the origin of the value of this VM option.

Returns the value of this VM option at the time when
this

VMOption

was created.

Tests if this VM option is writeable.

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

- VMOption

```java
public VMOption​(
String
name,

String
value,
boolean writeable,

VMOption.Origin
origin)
```

Constructs a

VMOption

.

**Parameters:** name

- Name of a VM option.
**Parameters:** value

- Value of a VM option.
**Parameters:** writeable

-

true

if a VM option can be set dynamically,
or

false

otherwise.
**Parameters:** origin

- where the value of a VM option came from.
**Throws:** NullPointerException

- if the name or value is

null

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the name of this VM option.

**Returns:** the name of this VM option.

- getValue

```java
public
String
getValue()
```

Returns the value of this VM option at the time when
this

VMOption

was created. The value could have been changed.

**Returns:** the value of the VM option at the time when
this

VMOption

was created.

- getOrigin

```java
public
VMOption.Origin
getOrigin()
```

Returns the origin of the value of this VM option. That is,
where the value of this VM option came from.

**Returns:** where the value of this VM option came from.

- isWriteable

```java
public boolean isWriteable()
```

Tests if this VM option is writeable. If this VM option is writeable,
it can be set by the

HotSpotDiagnosticMXBean.setVMOption

method.

**Returns:** true

if this VM option is writeable;

false

otherwise.

- from

```java
public static
VMOption
from​(
CompositeData
cd)
```

Returns a

VMOption

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

description

Attribute Name

Type

name

java.lang.String

value

java.lang.String

origin

java.lang.String

writeable

java.lang.Boolean

**Parameters:** cd

-

CompositeData

representing a

VMOption
**Returns:** a

VMOption

object represented by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

VMOption

with the attributes described
above.

Constructor Detail

- VMOption

```java
public VMOption​(
String
name,

String
value,
boolean writeable,

VMOption.Origin
origin)
```

Constructs a

VMOption

.

**Parameters:** name

- Name of a VM option.
**Parameters:** value

- Value of a VM option.
**Parameters:** writeable

-

true

if a VM option can be set dynamically,
or

false

otherwise.
**Parameters:** origin

- where the value of a VM option came from.
**Throws:** NullPointerException

- if the name or value is

null

---

#### Constructor Detail

VMOption

```java
public VMOption​(
String
name,

String
value,
boolean writeable,

VMOption.Origin
origin)
```

Constructs a

VMOption

.

**Parameters:** name

- Name of a VM option.
**Parameters:** value

- Value of a VM option.
**Parameters:** writeable

-

true

if a VM option can be set dynamically,
or

false

otherwise.
**Parameters:** origin

- where the value of a VM option came from.
**Throws:** NullPointerException

- if the name or value is

null

---

#### VMOption

public VMOption​(

String

name,

String

value,
boolean writeable,

VMOption.Origin

origin)

Constructs a

VMOption

.

Method Detail

- getName

```java
public
String
getName()
```

Returns the name of this VM option.

**Returns:** the name of this VM option.

- getValue

```java
public
String
getValue()
```

Returns the value of this VM option at the time when
this

VMOption

was created. The value could have been changed.

**Returns:** the value of the VM option at the time when
this

VMOption

was created.

- getOrigin

```java
public
VMOption.Origin
getOrigin()
```

Returns the origin of the value of this VM option. That is,
where the value of this VM option came from.

**Returns:** where the value of this VM option came from.

- isWriteable

```java
public boolean isWriteable()
```

Tests if this VM option is writeable. If this VM option is writeable,
it can be set by the

HotSpotDiagnosticMXBean.setVMOption

method.

**Returns:** true

if this VM option is writeable;

false

otherwise.

- from

```java
public static
VMOption
from​(
CompositeData
cd)
```

Returns a

VMOption

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

description

Attribute Name

Type

name

java.lang.String

value

java.lang.String

origin

java.lang.String

writeable

java.lang.Boolean

**Parameters:** cd

-

CompositeData

representing a

VMOption
**Returns:** a

VMOption

object represented by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

VMOption

with the attributes described
above.

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the name of this VM option.

**Returns:** the name of this VM option.

---

#### getName

public

String

getName()

Returns the name of this VM option.

getValue

```java
public
String
getValue()
```

Returns the value of this VM option at the time when
this

VMOption

was created. The value could have been changed.

**Returns:** the value of the VM option at the time when
this

VMOption

was created.

---

#### getValue

public

String

getValue()

Returns the value of this VM option at the time when
this

VMOption

was created. The value could have been changed.

getOrigin

```java
public
VMOption.Origin
getOrigin()
```

Returns the origin of the value of this VM option. That is,
where the value of this VM option came from.

**Returns:** where the value of this VM option came from.

---

#### getOrigin

public

VMOption.Origin

getOrigin()

Returns the origin of the value of this VM option. That is,
where the value of this VM option came from.

isWriteable

```java
public boolean isWriteable()
```

Tests if this VM option is writeable. If this VM option is writeable,
it can be set by the

HotSpotDiagnosticMXBean.setVMOption

method.

**Returns:** true

if this VM option is writeable;

false

otherwise.

---

#### isWriteable

public boolean isWriteable()

Tests if this VM option is writeable. If this VM option is writeable,
it can be set by the

HotSpotDiagnosticMXBean.setVMOption

method.

from

```java
public static
VMOption
from​(
CompositeData
cd)
```

Returns a

VMOption

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

description

Attribute Name

Type

name

java.lang.String

value

java.lang.String

origin

java.lang.String

writeable

java.lang.Boolean

**Parameters:** cd

-

CompositeData

representing a

VMOption
**Returns:** a

VMOption

object represented by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

VMOption

with the attributes described
above.

---

#### from

public static

VMOption

from​(

CompositeData

cd)

Returns a

VMOption

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

description

Attribute Name

Type

name

java.lang.String

value

java.lang.String

origin

java.lang.String

writeable

java.lang.Boolean

---

