# Enum DrbgParameters.Capability

**Source:** `java.base\java\security\DrbgParameters.Capability.html`

### Class Description

```java
public static enum
DrbgParameters.Capability

extends
Enum
<
DrbgParameters.Capability
>
```

The reseedable and prediction resistance capabilities of a DRBG.

When this object is passed to a

SecureRandom.getInstance()

call,
it is the requested minimum capability. When it's returned from

SecureRandom.getParameters()

, it is the effective capability.

Please note that while the

Instantiate_function

defined in
NIST SP 800-90Ar1 only includes a

prediction_resistance_flag

parameter, the

Capability

type includes an extra value

RESEED_ONLY

because reseeding is an optional function.
If

NONE

is used in an

Instantiation

object in calling the

SecureRandom.getInstance

method, the returned DRBG instance
is not guaranteed to support reseeding. If

RESEED_ONLY

or

PR_AND_RESEED

is used, the instance must support reseeding.

The table below lists possible effective values if a certain
capability is requested, i.e.

```java
Capability requested = ...;
SecureRandom s = SecureRandom.getInstance("DRBG",
DrbgParameters(-1, requested, null));
Capability effective = ((DrbgParametes.Initiate) s.getParameters())
.getCapability();
```

requested and effective capabilities

Requested Value

Possible Effective Values

NONE

NONE, RESEED_ONLY, PR_AND_RESEED

RESEED_ONLY

RESEED_ONLY, PR_AND_RESEED

PR_AND_RESEED

PR_AND_RESEED

A DRBG implementation supporting prediction resistance must also
support reseeding.

**All Implemented Interfaces:** Serializable

,

Comparable

<

DrbgParameters.Capability

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
DrbgParameters.Capability
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DrbgParameters.Capability c : DrbgParameters.Capability.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
DrbgParameters.Capability
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

#### public boolean supportsReseeding()

Returns whether this capability supports reseeding.

**Returns:**
- true

for

PR_AND_RESEED

and

RESEED_ONLY

, and

false

for

NONE

---

#### public boolean supportsPredictionResistance()

Returns whether this capability supports prediction resistance.

**Returns:**
- true

for

PR_AND_RESEED

, and

false

for

RESEED_ONLY

and

NONE

---

### Additional Sections

#### Enum DrbgParameters.Capability

java.lang.Object

- java.lang.Enum

<

DrbgParameters.Capability

>
- - java.security.DrbgParameters.Capability

java.lang.Enum

<

DrbgParameters.Capability

>

- java.security.DrbgParameters.Capability

java.security.DrbgParameters.Capability

**All Implemented Interfaces:** Serializable

,

Comparable

<

DrbgParameters.Capability

>

**Enclosing class:** DrbgParameters

```java
public static enum
DrbgParameters.Capability

extends
Enum
<
DrbgParameters.Capability
>
```

The reseedable and prediction resistance capabilities of a DRBG.

When this object is passed to a

SecureRandom.getInstance()

call,
it is the requested minimum capability. When it's returned from

SecureRandom.getParameters()

, it is the effective capability.

Please note that while the

Instantiate_function

defined in
NIST SP 800-90Ar1 only includes a

prediction_resistance_flag

parameter, the

Capability

type includes an extra value

RESEED_ONLY

because reseeding is an optional function.
If

NONE

is used in an

Instantiation

object in calling the

SecureRandom.getInstance

method, the returned DRBG instance
is not guaranteed to support reseeding. If

RESEED_ONLY

or

PR_AND_RESEED

is used, the instance must support reseeding.

The table below lists possible effective values if a certain
capability is requested, i.e.

```java
Capability requested = ...;
SecureRandom s = SecureRandom.getInstance("DRBG",
DrbgParameters(-1, requested, null));
Capability effective = ((DrbgParametes.Initiate) s.getParameters())
.getCapability();
```

requested and effective capabilities

Requested Value

Possible Effective Values

NONE

NONE, RESEED_ONLY, PR_AND_RESEED

RESEED_ONLY

RESEED_ONLY, PR_AND_RESEED

PR_AND_RESEED

PR_AND_RESEED

A DRBG implementation supporting prediction resistance must also
support reseeding.

**Since:** 9

public static enum

DrbgParameters.Capability

extends

Enum

<

DrbgParameters.Capability

>

The reseedable and prediction resistance capabilities of a DRBG.

When this object is passed to a

SecureRandom.getInstance()

call,
it is the requested minimum capability. When it's returned from

SecureRandom.getParameters()

, it is the effective capability.

Please note that while the

Instantiate_function

defined in
NIST SP 800-90Ar1 only includes a

prediction_resistance_flag

parameter, the

Capability

type includes an extra value

RESEED_ONLY

because reseeding is an optional function.
If

NONE

is used in an

Instantiation

object in calling the

SecureRandom.getInstance

method, the returned DRBG instance
is not guaranteed to support reseeding. If

RESEED_ONLY

or

PR_AND_RESEED

is used, the instance must support reseeding.

The table below lists possible effective values if a certain
capability is requested, i.e.

```java
Capability requested = ...;
SecureRandom s = SecureRandom.getInstance("DRBG",
DrbgParameters(-1, requested, null));
Capability effective = ((DrbgParametes.Initiate) s.getParameters())
.getCapability();
```

requested and effective capabilities

Requested Value

Possible Effective Values

NONE

NONE, RESEED_ONLY, PR_AND_RESEED

RESEED_ONLY

RESEED_ONLY, PR_AND_RESEED

PR_AND_RESEED

PR_AND_RESEED

A DRBG implementation supporting prediction resistance must also
support reseeding.

When this object is passed to a

SecureRandom.getInstance()

call,
it is the requested minimum capability. When it's returned from

SecureRandom.getParameters()

, it is the effective capability.

Please note that while the

Instantiate_function

defined in
NIST SP 800-90Ar1 only includes a

prediction_resistance_flag

parameter, the

Capability

type includes an extra value

RESEED_ONLY

because reseeding is an optional function.
If

NONE

is used in an

Instantiation

object in calling the

SecureRandom.getInstance

method, the returned DRBG instance
is not guaranteed to support reseeding. If

RESEED_ONLY

or

PR_AND_RESEED

is used, the instance must support reseeding.

The table below lists possible effective values if a certain
capability is requested, i.e.

```java
Capability requested = ...;
SecureRandom s = SecureRandom.getInstance("DRBG",
DrbgParameters(-1, requested, null));
Capability effective = ((DrbgParametes.Initiate) s.getParameters())
.getCapability();
```

requested and effective capabilities

Requested Value

Possible Effective Values

NONE

NONE, RESEED_ONLY, PR_AND_RESEED

RESEED_ONLY

RESEED_ONLY, PR_AND_RESEED

PR_AND_RESEED

PR_AND_RESEED

A DRBG implementation supporting prediction resistance must also
support reseeding.

Please note that while the

Instantiate_function

defined in
NIST SP 800-90Ar1 only includes a

prediction_resistance_flag

parameter, the

Capability

type includes an extra value

RESEED_ONLY

because reseeding is an optional function.
If

NONE

is used in an

Instantiation

object in calling the

SecureRandom.getInstance

method, the returned DRBG instance
is not guaranteed to support reseeding. If

RESEED_ONLY

or

PR_AND_RESEED

is used, the instance must support reseeding.

The table below lists possible effective values if a certain
capability is requested, i.e.

```java
Capability requested = ...;
SecureRandom s = SecureRandom.getInstance("DRBG",
DrbgParameters(-1, requested, null));
Capability effective = ((DrbgParametes.Initiate) s.getParameters())
.getCapability();
```

requested and effective capabilities

Requested Value

Possible Effective Values

NONE

NONE, RESEED_ONLY, PR_AND_RESEED

RESEED_ONLY

RESEED_ONLY, PR_AND_RESEED

PR_AND_RESEED

PR_AND_RESEED

A DRBG implementation supporting prediction resistance must also
support reseeding.

The table below lists possible effective values if a certain
capability is requested, i.e.

```java
Capability requested = ...;
SecureRandom s = SecureRandom.getInstance("DRBG",
DrbgParameters(-1, requested, null));
Capability effective = ((DrbgParametes.Initiate) s.getParameters())
.getCapability();
```

requested and effective capabilities

Requested Value

Possible Effective Values

NONE

NONE, RESEED_ONLY, PR_AND_RESEED

RESEED_ONLY

RESEED_ONLY, PR_AND_RESEED

PR_AND_RESEED

PR_AND_RESEED

A DRBG implementation supporting prediction resistance must also
support reseeding.

Capability requested = ...;
SecureRandom s = SecureRandom.getInstance("DRBG",
DrbgParameters(-1, requested, null));
Capability effective = ((DrbgParametes.Initiate) s.getParameters())
.getCapability();

A DRBG implementation supporting prediction resistance must also
support reseeding.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

NONE

Neither prediction resistance nor reseed.

PR_AND_RESEED

Both prediction resistance and reseed.

RESEED_ONLY

Reseed but no prediction resistance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

supportsPredictionResistance

()

Returns whether this capability supports prediction resistance.

boolean

supportsReseeding

()

Returns whether this capability supports reseeding.

static

DrbgParameters.Capability

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

DrbgParameters.Capability

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

NONE

Neither prediction resistance nor reseed.

PR_AND_RESEED

Both prediction resistance and reseed.

RESEED_ONLY

Reseed but no prediction resistance.

---

#### Enum Constant Summary

Neither prediction resistance nor reseed.

Both prediction resistance and reseed.

Reseed but no prediction resistance.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

supportsPredictionResistance

()

Returns whether this capability supports prediction resistance.

boolean

supportsReseeding

()

Returns whether this capability supports reseeding.

static

DrbgParameters.Capability

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

DrbgParameters.Capability

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

Returns whether this capability supports prediction resistance.

Returns whether this capability supports reseeding.

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- PR_AND_RESEED

```java
public static final
DrbgParameters.Capability
PR_AND_RESEED
```

Both prediction resistance and reseed.

- RESEED_ONLY

```java
public static final
DrbgParameters.Capability
RESEED_ONLY
```

Reseed but no prediction resistance.

- NONE

```java
public static final
DrbgParameters.Capability
NONE
```

Neither prediction resistance nor reseed.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
DrbgParameters.Capability
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DrbgParameters.Capability c : DrbgParameters.Capability.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
DrbgParameters.Capability
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- supportsReseeding

```java
public boolean supportsReseeding()
```

Returns whether this capability supports reseeding.

**Returns:** true

for

PR_AND_RESEED

and

RESEED_ONLY

, and

false

for

NONE

- supportsPredictionResistance

```java
public boolean supportsPredictionResistance()
```

Returns whether this capability supports prediction resistance.

**Returns:** true

for

PR_AND_RESEED

, and

false

for

RESEED_ONLY

and

NONE

Enum Constant Detail

- PR_AND_RESEED

```java
public static final
DrbgParameters.Capability
PR_AND_RESEED
```

Both prediction resistance and reseed.

- RESEED_ONLY

```java
public static final
DrbgParameters.Capability
RESEED_ONLY
```

Reseed but no prediction resistance.

- NONE

```java
public static final
DrbgParameters.Capability
NONE
```

Neither prediction resistance nor reseed.

---

#### Enum Constant Detail

PR_AND_RESEED

```java
public static final
DrbgParameters.Capability
PR_AND_RESEED
```

Both prediction resistance and reseed.

---

#### PR_AND_RESEED

public static final

DrbgParameters.Capability

PR_AND_RESEED

Both prediction resistance and reseed.

RESEED_ONLY

```java
public static final
DrbgParameters.Capability
RESEED_ONLY
```

Reseed but no prediction resistance.

---

#### RESEED_ONLY

public static final

DrbgParameters.Capability

RESEED_ONLY

Reseed but no prediction resistance.

NONE

```java
public static final
DrbgParameters.Capability
NONE
```

Neither prediction resistance nor reseed.

---

#### NONE

public static final

DrbgParameters.Capability

NONE

Neither prediction resistance nor reseed.

Method Detail

- values

```java
public static
DrbgParameters.Capability
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DrbgParameters.Capability c : DrbgParameters.Capability.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
DrbgParameters.Capability
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- supportsReseeding

```java
public boolean supportsReseeding()
```

Returns whether this capability supports reseeding.

**Returns:** true

for

PR_AND_RESEED

and

RESEED_ONLY

, and

false

for

NONE

- supportsPredictionResistance

```java
public boolean supportsPredictionResistance()
```

Returns whether this capability supports prediction resistance.

**Returns:** true

for

PR_AND_RESEED

, and

false

for

RESEED_ONLY

and

NONE

---

#### Method Detail

values

```java
public static
DrbgParameters.Capability
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DrbgParameters.Capability c : DrbgParameters.Capability.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

DrbgParameters.Capability

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (DrbgParameters.Capability c : DrbgParameters.Capability.values())
System.out.println(c);
```

for (DrbgParameters.Capability c : DrbgParameters.Capability.values())
System.out.println(c);

valueOf

```java
public static
DrbgParameters.Capability
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

DrbgParameters.Capability

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

supportsReseeding

```java
public boolean supportsReseeding()
```

Returns whether this capability supports reseeding.

**Returns:** true

for

PR_AND_RESEED

and

RESEED_ONLY

, and

false

for

NONE

---

#### supportsReseeding

public boolean supportsReseeding()

Returns whether this capability supports reseeding.

supportsPredictionResistance

```java
public boolean supportsPredictionResistance()
```

Returns whether this capability supports prediction resistance.

**Returns:** true

for

PR_AND_RESEED

, and

false

for

RESEED_ONLY

and

NONE

---

#### supportsPredictionResistance

public boolean supportsPredictionResistance()

Returns whether this capability supports prediction resistance.

---

