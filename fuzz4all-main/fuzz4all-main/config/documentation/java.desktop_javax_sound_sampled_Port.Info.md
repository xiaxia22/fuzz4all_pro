# Class Port.Info

**Source:** `java.desktop\javax\sound\sampled\Port.Info.html`

### Class Description

```java
public static class
Port.Info

extends
Line.Info
```

The

Port.Info

class extends

Line.Info

with additional
information specific to ports, including the port's name and whether it
is a source or a target for its mixer. By definition, a port acts as
either a source or a target to its mixer, but not both. (Audio input
ports are sources; audio output ports are targets.)

To learn what ports are available, you can retrieve port info objects
through the

getSourceLineInfo

and

getTargetLineInfo

methods of the

Mixer

interface. Instances of the

Port.Info

class may
also be constructed and used to obtain lines matching the parameters
specified in the

Port.Info

object.

**Enclosing interface:** Port

---

### Field Details

#### public static final
Port.Info
MICROPHONE

A type of port that gets audio from a built-in microphone or a
microphone jack.

---

#### public static final
Port.Info
LINE_IN

A type of port that gets audio from a line-level audio input jack.

---

#### public static final
Port.Info
COMPACT_DISC

A type of port that gets audio from a CD-ROM drive.

---

#### public static final
Port.Info
SPEAKER

A type of port that sends audio to a built-in speaker or a speaker
jack.

---

#### public static final
Port.Info
HEADPHONE

A type of port that sends audio to a headphone jack.

---

#### public static final
Port.Info
LINE_OUT

A type of port that sends audio to a line-level audio output jack.

---

### Constructor Details

#### public Info​(
Class
<?> lineClass,

String
name,
boolean isSource)

Constructs a port's info object from the information given. This
constructor is typically used by an implementation of Java Sound to
describe a supported line.

**Parameters:**
- lineClass

- the class of the port described by the info object
- name

- the string that names the port
- isSource

-

true

if the port is a source port (such as a
microphone),

false

if the port is a target port (such
as a speaker)

---

### Method Details

#### public
String
getName()

Obtains the name of the port.

**Returns:**
- the string that names the port

---

#### public boolean isSource()

Indicates whether the port is a source or a target for its mixer.

**Returns:**
- true

if the port is a source port (such as a
microphone),

false

if the port is a target port (such
as a speaker)

---

#### public boolean matches​(
Line.Info
info)

Indicates whether this info object specified matches this one. To
match, the match requirements of the superclass must be met and the
types must be equal.

**Overrides:**
- matches

in class

Line.Info

**Parameters:**
- info

- the info object for which the match is queried

**Returns:**
- true

if the specified object matches this one,

false

otherwise

---

#### public final boolean equals​(
Object
obj)

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare

**Returns:**
- true

if the specified object is equal to this info
object;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns a hash code value for this info object.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this info object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public final
String
toString()

Provides a

String

representation of the port.

**Overrides:**
- toString

in class

Line.Info

**Returns:**
- a string that describes the port

---

### Additional Sections

#### Class Port.Info

java.lang.Object

- javax.sound.sampled.Line.Info
- - javax.sound.sampled.Port.Info

javax.sound.sampled.Line.Info

- javax.sound.sampled.Port.Info

javax.sound.sampled.Port.Info

**Enclosing interface:** Port

```java
public static class
Port.Info

extends
Line.Info
```

The

Port.Info

class extends

Line.Info

with additional
information specific to ports, including the port's name and whether it
is a source or a target for its mixer. By definition, a port acts as
either a source or a target to its mixer, but not both. (Audio input
ports are sources; audio output ports are targets.)

To learn what ports are available, you can retrieve port info objects
through the

getSourceLineInfo

and

getTargetLineInfo

methods of the

Mixer

interface. Instances of the

Port.Info

class may
also be constructed and used to obtain lines matching the parameters
specified in the

Port.Info

object.

**Since:** 1.3

public static class

Port.Info

extends

Line.Info

The

Port.Info

class extends

Line.Info

with additional
information specific to ports, including the port's name and whether it
is a source or a target for its mixer. By definition, a port acts as
either a source or a target to its mixer, but not both. (Audio input
ports are sources; audio output ports are targets.)

To learn what ports are available, you can retrieve port info objects
through the

getSourceLineInfo

and

getTargetLineInfo

methods of the

Mixer

interface. Instances of the

Port.Info

class may
also be constructed and used to obtain lines matching the parameters
specified in the

Port.Info

object.

To learn what ports are available, you can retrieve port info objects
through the

getSourceLineInfo

and

getTargetLineInfo

methods of the

Mixer

interface. Instances of the

Port.Info

class may
also be constructed and used to obtain lines matching the parameters
specified in the

Port.Info

object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Port.Info

COMPACT_DISC

A type of port that gets audio from a CD-ROM drive.

static

Port.Info

HEADPHONE

A type of port that sends audio to a headphone jack.

static

Port.Info

LINE_IN

A type of port that gets audio from a line-level audio input jack.

static

Port.Info

LINE_OUT

A type of port that sends audio to a line-level audio output jack.

static

Port.Info

MICROPHONE

A type of port that gets audio from a built-in microphone or a
microphone jack.

static

Port.Info

SPEAKER

A type of port that sends audio to a built-in speaker or a speaker
jack.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Info

​(

Class

<?> lineClass,

String

name,
boolean isSource)

Constructs a port's info object from the information given.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

String

getName

()

Obtains the name of the port.

int

hashCode

()

Returns a hash code value for this info object.

boolean

isSource

()

Indicates whether the port is a source or a target for its mixer.

boolean

matches

​(

Line.Info

info)

Indicates whether this info object specified matches this one.

String

toString

()

Provides a

String

representation of the port.

- Methods declared in class javax.sound.sampled.

Line.Info

getLineClass

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Field Summary

Fields

Modifier and Type

Field

Description

static

Port.Info

COMPACT_DISC

A type of port that gets audio from a CD-ROM drive.

static

Port.Info

HEADPHONE

A type of port that sends audio to a headphone jack.

static

Port.Info

LINE_IN

A type of port that gets audio from a line-level audio input jack.

static

Port.Info

LINE_OUT

A type of port that sends audio to a line-level audio output jack.

static

Port.Info

MICROPHONE

A type of port that gets audio from a built-in microphone or a
microphone jack.

static

Port.Info

SPEAKER

A type of port that sends audio to a built-in speaker or a speaker
jack.

---

#### Field Summary

A type of port that gets audio from a CD-ROM drive.

A type of port that sends audio to a headphone jack.

A type of port that gets audio from a line-level audio input jack.

A type of port that sends audio to a line-level audio output jack.

A type of port that gets audio from a built-in microphone or a
microphone jack.

A type of port that sends audio to a built-in speaker or a speaker
jack.

Constructor Summary

Constructors

Constructor

Description

Info

​(

Class

<?> lineClass,

String

name,
boolean isSource)

Constructs a port's info object from the information given.

---

#### Constructor Summary

Constructs a port's info object from the information given.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

String

getName

()

Obtains the name of the port.

int

hashCode

()

Returns a hash code value for this info object.

boolean

isSource

()

Indicates whether the port is a source or a target for its mixer.

boolean

matches

​(

Line.Info

info)

Indicates whether this info object specified matches this one.

String

toString

()

Provides a

String

representation of the port.

- Methods declared in class javax.sound.sampled.

Line.Info

getLineClass

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

Obtains the name of the port.

Returns a hash code value for this info object.

Indicates whether the port is a source or a target for its mixer.

Indicates whether this info object specified matches this one.

Provides a

String

representation of the port.

Methods declared in class javax.sound.sampled.

Line.Info

getLineClass

---

#### Methods declared in class javax.sound.sampled. Line.Info

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

============ FIELD DETAIL ===========

- Field Detail

- MICROPHONE

```java
public static final
Port.Info
MICROPHONE
```

A type of port that gets audio from a built-in microphone or a
microphone jack.

- LINE_IN

```java
public static final
Port.Info
LINE_IN
```

A type of port that gets audio from a line-level audio input jack.

- COMPACT_DISC

```java
public static final
Port.Info
COMPACT_DISC
```

A type of port that gets audio from a CD-ROM drive.

- SPEAKER

```java
public static final
Port.Info
SPEAKER
```

A type of port that sends audio to a built-in speaker or a speaker
jack.

- HEADPHONE

```java
public static final
Port.Info
HEADPHONE
```

A type of port that sends audio to a headphone jack.

- LINE_OUT

```java
public static final
Port.Info
LINE_OUT
```

A type of port that sends audio to a line-level audio output jack.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Info

```java
public Info​(
Class
<?> lineClass,

String
name,
boolean isSource)
```

Constructs a port's info object from the information given. This
constructor is typically used by an implementation of Java Sound to
describe a supported line.

**Parameters:** lineClass

- the class of the port described by the info object
**Parameters:** name

- the string that names the port
**Parameters:** isSource

-

true

if the port is a source port (such as a
microphone),

false

if the port is a target port (such
as a speaker)

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Obtains the name of the port.

**Returns:** the string that names the port

- isSource

```java
public boolean isSource()
```

Indicates whether the port is a source or a target for its mixer.

**Returns:** true

if the port is a source port (such as a
microphone),

false

if the port is a target port (such
as a speaker)

- matches

```java
public boolean matches​(
Line.Info
info)
```

Indicates whether this info object specified matches this one. To
match, the match requirements of the superclass must be met and the
types must be equal.

**Overrides:** matches

in class

Line.Info
**Parameters:** info

- the info object for which the match is queried
**Returns:** true

if the specified object matches this one,

false

otherwise

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this info
object;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this info object.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this info object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides a

String

representation of the port.

**Overrides:** toString

in class

Line.Info
**Returns:** a string that describes the port

Field Detail

- MICROPHONE

```java
public static final
Port.Info
MICROPHONE
```

A type of port that gets audio from a built-in microphone or a
microphone jack.

- LINE_IN

```java
public static final
Port.Info
LINE_IN
```

A type of port that gets audio from a line-level audio input jack.

- COMPACT_DISC

```java
public static final
Port.Info
COMPACT_DISC
```

A type of port that gets audio from a CD-ROM drive.

- SPEAKER

```java
public static final
Port.Info
SPEAKER
```

A type of port that sends audio to a built-in speaker or a speaker
jack.

- HEADPHONE

```java
public static final
Port.Info
HEADPHONE
```

A type of port that sends audio to a headphone jack.

- LINE_OUT

```java
public static final
Port.Info
LINE_OUT
```

A type of port that sends audio to a line-level audio output jack.

---

#### Field Detail

MICROPHONE

```java
public static final
Port.Info
MICROPHONE
```

A type of port that gets audio from a built-in microphone or a
microphone jack.

---

#### MICROPHONE

public static final

Port.Info

MICROPHONE

A type of port that gets audio from a built-in microphone or a
microphone jack.

LINE_IN

```java
public static final
Port.Info
LINE_IN
```

A type of port that gets audio from a line-level audio input jack.

---

#### LINE_IN

public static final

Port.Info

LINE_IN

A type of port that gets audio from a line-level audio input jack.

COMPACT_DISC

```java
public static final
Port.Info
COMPACT_DISC
```

A type of port that gets audio from a CD-ROM drive.

---

#### COMPACT_DISC

public static final

Port.Info

COMPACT_DISC

A type of port that gets audio from a CD-ROM drive.

SPEAKER

```java
public static final
Port.Info
SPEAKER
```

A type of port that sends audio to a built-in speaker or a speaker
jack.

---

#### SPEAKER

public static final

Port.Info

SPEAKER

A type of port that sends audio to a built-in speaker or a speaker
jack.

HEADPHONE

```java
public static final
Port.Info
HEADPHONE
```

A type of port that sends audio to a headphone jack.

---

#### HEADPHONE

public static final

Port.Info

HEADPHONE

A type of port that sends audio to a headphone jack.

LINE_OUT

```java
public static final
Port.Info
LINE_OUT
```

A type of port that sends audio to a line-level audio output jack.

---

#### LINE_OUT

public static final

Port.Info

LINE_OUT

A type of port that sends audio to a line-level audio output jack.

Constructor Detail

- Info

```java
public Info​(
Class
<?> lineClass,

String
name,
boolean isSource)
```

Constructs a port's info object from the information given. This
constructor is typically used by an implementation of Java Sound to
describe a supported line.

**Parameters:** lineClass

- the class of the port described by the info object
**Parameters:** name

- the string that names the port
**Parameters:** isSource

-

true

if the port is a source port (such as a
microphone),

false

if the port is a target port (such
as a speaker)

---

#### Constructor Detail

Info

```java
public Info​(
Class
<?> lineClass,

String
name,
boolean isSource)
```

Constructs a port's info object from the information given. This
constructor is typically used by an implementation of Java Sound to
describe a supported line.

**Parameters:** lineClass

- the class of the port described by the info object
**Parameters:** name

- the string that names the port
**Parameters:** isSource

-

true

if the port is a source port (such as a
microphone),

false

if the port is a target port (such
as a speaker)

---

#### Info

public Info​(

Class

<?> lineClass,

String

name,
boolean isSource)

Constructs a port's info object from the information given. This
constructor is typically used by an implementation of Java Sound to
describe a supported line.

Method Detail

- getName

```java
public
String
getName()
```

Obtains the name of the port.

**Returns:** the string that names the port

- isSource

```java
public boolean isSource()
```

Indicates whether the port is a source or a target for its mixer.

**Returns:** true

if the port is a source port (such as a
microphone),

false

if the port is a target port (such
as a speaker)

- matches

```java
public boolean matches​(
Line.Info
info)
```

Indicates whether this info object specified matches this one. To
match, the match requirements of the superclass must be met and the
types must be equal.

**Overrides:** matches

in class

Line.Info
**Parameters:** info

- the info object for which the match is queried
**Returns:** true

if the specified object matches this one,

false

otherwise

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this info
object;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this info object.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this info object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides a

String

representation of the port.

**Overrides:** toString

in class

Line.Info
**Returns:** a string that describes the port

---

#### Method Detail

getName

```java
public
String
getName()
```

Obtains the name of the port.

**Returns:** the string that names the port

---

#### getName

public

String

getName()

Obtains the name of the port.

isSource

```java
public boolean isSource()
```

Indicates whether the port is a source or a target for its mixer.

**Returns:** true

if the port is a source port (such as a
microphone),

false

if the port is a target port (such
as a speaker)

---

#### isSource

public boolean isSource()

Indicates whether the port is a source or a target for its mixer.

matches

```java
public boolean matches​(
Line.Info
info)
```

Indicates whether this info object specified matches this one. To
match, the match requirements of the superclass must be met and the
types must be equal.

**Overrides:** matches

in class

Line.Info
**Parameters:** info

- the info object for which the match is queried
**Returns:** true

if the specified object matches this one,

false

otherwise

---

#### matches

public boolean matches​(

Line.Info

info)

Indicates whether this info object specified matches this one. To
match, the match requirements of the superclass must be met and the
types must be equal.

equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this info
object;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Indicates whether the specified object is equal to this info object,
returning

true

if the objects are the same.

hashCode

```java
public final int hashCode()
```

Returns a hash code value for this info object.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this info object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hash code value for this info object.

toString

```java
public final
String
toString()
```

Provides a

String

representation of the port.

**Overrides:** toString

in class

Line.Info
**Returns:** a string that describes the port

---

#### toString

public final

String

toString()

Provides a

String

representation of the port.

---

