# Class MixerProvider

**Source:** `java.desktop\javax\sound\sampled\spi\MixerProvider.html`

### Class Description

```java
public abstract class
MixerProvider

extends
Object
```

A provider or factory for a particular mixer type. This mechanism allows the
implementation to determine how resources are managed in creation /
management of a mixer.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### public MixerProvider()

*No description found.*

---

### Method Details

#### public boolean isMixerSupported​(
Mixer.Info
info)

Indicates whether the mixer provider supports the mixer represented by
the specified mixer info object.

The full set of mixer info objects that represent the mixers supported by
this

MixerProvider

may be obtained through the

getMixerInfo

method.

**Parameters:**
- info

- an info object that describes the mixer for which support is
queried

**Returns:**
- true

if the specified mixer is supported, otherwise

false

**Throws:**
- NullPointerException

- if

info

is

null

**See Also:**
- getMixerInfo()

---

#### public abstract
Mixer.Info
[] getMixerInfo()

Obtains the set of info objects representing the mixer or mixers provided
by this MixerProvider.

The

isMixerSupported

method returns

true

for all the info
objects returned by this method. The corresponding mixer instances for
the info objects are returned by the

getMixer

method.

**Returns:**
- a set of mixer info objects

**See Also:**
- getMixer(Mixer.Info)

,

isMixerSupported(Mixer.Info)

---

#### public abstract
Mixer
getMixer​(
Mixer.Info
info)

Obtains an instance of the mixer represented by the info object. If

null

is passed, then the default mixer will be returned.

The full set of the mixer info objects that represent the mixers
supported by this

MixerProvider

may be obtained through the

getMixerInfo

method. Use the

isMixerSupported

method to
test whether this

MixerProvider

supports a particular mixer.

**Parameters:**
- info

- an info object that describes the desired mixer, or

null

for the default mixer

**Returns:**
- mixer instance

**Throws:**
- IllegalArgumentException

- if the info object specified does not
match the info object for a mixer supported by this

MixerProvider

, or if this

MixerProvider

does not
have default mixer, but default mixer has been requested

**See Also:**
- getMixerInfo()

,

isMixerSupported(Mixer.Info)

---

### Additional Sections

#### Class MixerProvider

java.lang.Object

- javax.sound.sampled.spi.MixerProvider

javax.sound.sampled.spi.MixerProvider

```java
public abstract class
MixerProvider

extends
Object
```

A provider or factory for a particular mixer type. This mechanism allows the
implementation to determine how resources are managed in creation /
management of a mixer.

**Since:** 1.3

public abstract class

MixerProvider

extends

Object

A provider or factory for a particular mixer type. This mechanism allows the
implementation to determine how resources are managed in creation /
management of a mixer.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MixerProvider

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Mixer

getMixer

​(

Mixer.Info

info)

Obtains an instance of the mixer represented by the info object.

abstract

Mixer.Info

[]

getMixerInfo

()

Obtains the set of info objects representing the mixer or mixers provided
by this MixerProvider.

boolean

isMixerSupported

​(

Mixer.Info

info)

Indicates whether the mixer provider supports the mixer represented by
the specified mixer info object.

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

MixerProvider

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Mixer

getMixer

​(

Mixer.Info

info)

Obtains an instance of the mixer represented by the info object.

abstract

Mixer.Info

[]

getMixerInfo

()

Obtains the set of info objects representing the mixer or mixers provided
by this MixerProvider.

boolean

isMixerSupported

​(

Mixer.Info

info)

Indicates whether the mixer provider supports the mixer represented by
the specified mixer info object.

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

Obtains an instance of the mixer represented by the info object.

Obtains the set of info objects representing the mixer or mixers provided
by this MixerProvider.

Indicates whether the mixer provider supports the mixer represented by
the specified mixer info object.

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

- MixerProvider

```java
public MixerProvider()
```

============ METHOD DETAIL ==========

- Method Detail

- isMixerSupported

```java
public boolean isMixerSupported​(
Mixer.Info
info)
```

Indicates whether the mixer provider supports the mixer represented by
the specified mixer info object.

The full set of mixer info objects that represent the mixers supported by
this

MixerProvider

may be obtained through the

getMixerInfo

method.

**Parameters:** info

- an info object that describes the mixer for which support is
queried
**Returns:** true

if the specified mixer is supported, otherwise

false
**Throws:** NullPointerException

- if

info

is

null
**See Also:** getMixerInfo()

- getMixerInfo

```java
public abstract
Mixer.Info
[] getMixerInfo()
```

Obtains the set of info objects representing the mixer or mixers provided
by this MixerProvider.

The

isMixerSupported

method returns

true

for all the info
objects returned by this method. The corresponding mixer instances for
the info objects are returned by the

getMixer

method.

**Returns:** a set of mixer info objects
**See Also:** getMixer(Mixer.Info)

,

isMixerSupported(Mixer.Info)

- getMixer

```java
public abstract
Mixer
getMixer​(
Mixer.Info
info)
```

Obtains an instance of the mixer represented by the info object. If

null

is passed, then the default mixer will be returned.

The full set of the mixer info objects that represent the mixers
supported by this

MixerProvider

may be obtained through the

getMixerInfo

method. Use the

isMixerSupported

method to
test whether this

MixerProvider

supports a particular mixer.

**Parameters:** info

- an info object that describes the desired mixer, or

null

for the default mixer
**Returns:** mixer instance
**Throws:** IllegalArgumentException

- if the info object specified does not
match the info object for a mixer supported by this

MixerProvider

, or if this

MixerProvider

does not
have default mixer, but default mixer has been requested
**See Also:** getMixerInfo()

,

isMixerSupported(Mixer.Info)

Constructor Detail

- MixerProvider

```java
public MixerProvider()
```

---

#### Constructor Detail

MixerProvider

```java
public MixerProvider()
```

---

#### MixerProvider

public MixerProvider()

Method Detail

- isMixerSupported

```java
public boolean isMixerSupported​(
Mixer.Info
info)
```

Indicates whether the mixer provider supports the mixer represented by
the specified mixer info object.

The full set of mixer info objects that represent the mixers supported by
this

MixerProvider

may be obtained through the

getMixerInfo

method.

**Parameters:** info

- an info object that describes the mixer for which support is
queried
**Returns:** true

if the specified mixer is supported, otherwise

false
**Throws:** NullPointerException

- if

info

is

null
**See Also:** getMixerInfo()

- getMixerInfo

```java
public abstract
Mixer.Info
[] getMixerInfo()
```

Obtains the set of info objects representing the mixer or mixers provided
by this MixerProvider.

The

isMixerSupported

method returns

true

for all the info
objects returned by this method. The corresponding mixer instances for
the info objects are returned by the

getMixer

method.

**Returns:** a set of mixer info objects
**See Also:** getMixer(Mixer.Info)

,

isMixerSupported(Mixer.Info)

- getMixer

```java
public abstract
Mixer
getMixer​(
Mixer.Info
info)
```

Obtains an instance of the mixer represented by the info object. If

null

is passed, then the default mixer will be returned.

The full set of the mixer info objects that represent the mixers
supported by this

MixerProvider

may be obtained through the

getMixerInfo

method. Use the

isMixerSupported

method to
test whether this

MixerProvider

supports a particular mixer.

**Parameters:** info

- an info object that describes the desired mixer, or

null

for the default mixer
**Returns:** mixer instance
**Throws:** IllegalArgumentException

- if the info object specified does not
match the info object for a mixer supported by this

MixerProvider

, or if this

MixerProvider

does not
have default mixer, but default mixer has been requested
**See Also:** getMixerInfo()

,

isMixerSupported(Mixer.Info)

---

#### Method Detail

isMixerSupported

```java
public boolean isMixerSupported​(
Mixer.Info
info)
```

Indicates whether the mixer provider supports the mixer represented by
the specified mixer info object.

The full set of mixer info objects that represent the mixers supported by
this

MixerProvider

may be obtained through the

getMixerInfo

method.

**Parameters:** info

- an info object that describes the mixer for which support is
queried
**Returns:** true

if the specified mixer is supported, otherwise

false
**Throws:** NullPointerException

- if

info

is

null
**See Also:** getMixerInfo()

---

#### isMixerSupported

public boolean isMixerSupported​(

Mixer.Info

info)

Indicates whether the mixer provider supports the mixer represented by
the specified mixer info object.

The full set of mixer info objects that represent the mixers supported by
this

MixerProvider

may be obtained through the

getMixerInfo

method.

The full set of mixer info objects that represent the mixers supported by
this

MixerProvider

may be obtained through the

getMixerInfo

method.

getMixerInfo

```java
public abstract
Mixer.Info
[] getMixerInfo()
```

Obtains the set of info objects representing the mixer or mixers provided
by this MixerProvider.

The

isMixerSupported

method returns

true

for all the info
objects returned by this method. The corresponding mixer instances for
the info objects are returned by the

getMixer

method.

**Returns:** a set of mixer info objects
**See Also:** getMixer(Mixer.Info)

,

isMixerSupported(Mixer.Info)

---

#### getMixerInfo

public abstract

Mixer.Info

[] getMixerInfo()

Obtains the set of info objects representing the mixer or mixers provided
by this MixerProvider.

The

isMixerSupported

method returns

true

for all the info
objects returned by this method. The corresponding mixer instances for
the info objects are returned by the

getMixer

method.

The

isMixerSupported

method returns

true

for all the info
objects returned by this method. The corresponding mixer instances for
the info objects are returned by the

getMixer

method.

getMixer

```java
public abstract
Mixer
getMixer​(
Mixer.Info
info)
```

Obtains an instance of the mixer represented by the info object. If

null

is passed, then the default mixer will be returned.

The full set of the mixer info objects that represent the mixers
supported by this

MixerProvider

may be obtained through the

getMixerInfo

method. Use the

isMixerSupported

method to
test whether this

MixerProvider

supports a particular mixer.

**Parameters:** info

- an info object that describes the desired mixer, or

null

for the default mixer
**Returns:** mixer instance
**Throws:** IllegalArgumentException

- if the info object specified does not
match the info object for a mixer supported by this

MixerProvider

, or if this

MixerProvider

does not
have default mixer, but default mixer has been requested
**See Also:** getMixerInfo()

,

isMixerSupported(Mixer.Info)

---

#### getMixer

public abstract

Mixer

getMixer​(

Mixer.Info

info)

Obtains an instance of the mixer represented by the info object. If

null

is passed, then the default mixer will be returned.

The full set of the mixer info objects that represent the mixers
supported by this

MixerProvider

may be obtained through the

getMixerInfo

method. Use the

isMixerSupported

method to
test whether this

MixerProvider

supports a particular mixer.

The full set of the mixer info objects that represent the mixers
supported by this

MixerProvider

may be obtained through the

getMixerInfo

method. Use the

isMixerSupported

method to
test whether this

MixerProvider

supports a particular mixer.

---

