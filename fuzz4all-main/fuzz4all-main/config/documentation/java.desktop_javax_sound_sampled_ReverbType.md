# Class ReverbType

**Source:** `java.desktop\javax\sound\sampled\ReverbType.html`

### Class Description

```java
public class
ReverbType

extends
Object
```

The

ReverbType

class provides methods for accessing various
reverberation settings to be applied to an audio signal.

Reverberation simulates the reflection of sound off of the walls, ceiling,
and floor of a room. Depending on the size of the room, and how absorbent or
reflective the materials in the room's surfaces are, the sound might bounce
around for a long time before dying away.

The reverberation parameters provided by

ReverbType

consist of the
delay time and intensity of early reflections, the delay time and intensity
of late reflections, and an overall decay time. Early reflections are the
initial individual low-order reflections of the direct signal off the
surfaces in the room. The late reflections are the dense, high-order
reflections that characterize the room's reverberation. The delay times for
the start of these two reflection types give the listener a sense of the
overall size and complexity of the room's shape and contents. The larger the
room, the longer the reflection delay times. The early and late reflections'
intensities define the gain (in decibels) of the reflected signals as
compared to the direct signal. These intensities give the listener an
impression of the absorptive nature of the surfaces and objects in the room.
The decay time defines how long the reverberation takes to exponentially
decay until it is no longer perceptible ("effective zero"). The larger and
less absorbent the surfaces, the longer the decay time.

The set of parameters defined here may not include all aspects of
reverberation as specified by some systems. For example, the Midi
Manufacturer's Association (MMA) has an Interactive Audio Special Interest
Group (IASIG), which has a 3-D Working Group that has defined a Level 2 Spec
(I3DL2). I3DL2 supports filtering of reverberation and control of reverb
density. These properties are not included in the JavaSound 1.0 definition of
a reverb control. In such a case, the implementing system should either
extend the defined reverb control to include additional parameters, or else
interpret the system's additional capabilities in a way that fits the model
described here.

If implementing JavaSound on a I3DL2-compliant device:

- Filtering is disabled (high-frequency attenuations are set to 0.0 dB)

Density parameters are set to midway between minimum and maximum

The following table shows what parameter values an implementation might use
for a representative set of reverberation settings.

Reverb types and params: decay time, late intensity, late delay,
early intensity, and early delay

Type

Decay Time (ms)

Late Intensity (dB)

Late Delay (ms)

Early Intensity (dB)

Early Delay(ms)

Cavern

2250

-2.0

41.3

-1.4

10.3

Dungeon

1600

-1.0

10.3

-0.7

2.6

Garage

900

-6.0

14.7

-4.0

3.9

Acoustic Lab

280

-3.0

8.0

-2.0

2.0

Closet

150

-10.0

2.5

-7.0

0.6

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ReverbType​(
String
name,
int earlyReflectionDelay,
float earlyReflectionIntensity,
int lateReflectionDelay,
float lateReflectionIntensity,
int decayTime)

Constructs a new reverb type that has the specified reverberation
parameter values.

**Parameters:**
- name

- the name of the new reverb type, or a zero-length

String
- earlyReflectionDelay

- the new type's early reflection delay time
in microseconds
- earlyReflectionIntensity

- the new type's early reflection
intensity in dB
- lateReflectionDelay

- the new type's late reflection delay time in
microseconds
- lateReflectionIntensity

- the new type's late reflection intensity
in dB
- decayTime

- the new type's decay time in microseconds

---

### Method Details

#### public
String
getName()

Obtains the name of this reverb type.

**Returns:**
- the name of this reverb type

**Since:**
- 1.5

---

#### public final int getEarlyReflectionDelay()

Returns the early reflection delay time in microseconds. This is the
amount of time between when the direct signal is heard and when the first
early reflections are heard.

**Returns:**
- early reflection delay time for this reverb type, in microseconds

---

#### public final float getEarlyReflectionIntensity()

Returns the early reflection intensity in decibels. This is the amplitude
attenuation of the first early reflections relative to the direct signal.

**Returns:**
- early reflection intensity for this reverb type, in dB

---

#### public final int getLateReflectionDelay()

Returns the late reflection delay time in microseconds. This is the
amount of time between when the first early reflections are heard and
when the first late reflections are heard.

**Returns:**
- late reflection delay time for this reverb type, in microseconds

---

#### public final float getLateReflectionIntensity()

Returns the late reflection intensity in decibels. This is the amplitude
attenuation of the first late reflections relative to the direct signal.

**Returns:**
- late reflection intensity for this reverb type, in dB

---

#### public final int getDecayTime()

Obtains the decay time, which is the amount of time over which the late
reflections attenuate to effective zero. The effective zero value is
implementation-dependent.

**Returns:**
- the decay time of the late reflections, in microseconds

---

#### public final boolean equals​(
Object
obj)

Indicates whether the specified object is equal to this reverb type,
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

if the specified object is equal to this reverb
type;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns a hash code value for this reverb type.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this reverb type

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

representation of the reverb type, including
its name and its parameter settings. The exact contents of the string may
vary between implementations of Java Sound.

**Overrides:**
- toString

in class

Object

**Returns:**
- reverberation type name and description

---

### Additional Sections

#### Class ReverbType

java.lang.Object

- javax.sound.sampled.ReverbType

javax.sound.sampled.ReverbType

```java
public class
ReverbType

extends
Object
```

The

ReverbType

class provides methods for accessing various
reverberation settings to be applied to an audio signal.

Reverberation simulates the reflection of sound off of the walls, ceiling,
and floor of a room. Depending on the size of the room, and how absorbent or
reflective the materials in the room's surfaces are, the sound might bounce
around for a long time before dying away.

The reverberation parameters provided by

ReverbType

consist of the
delay time and intensity of early reflections, the delay time and intensity
of late reflections, and an overall decay time. Early reflections are the
initial individual low-order reflections of the direct signal off the
surfaces in the room. The late reflections are the dense, high-order
reflections that characterize the room's reverberation. The delay times for
the start of these two reflection types give the listener a sense of the
overall size and complexity of the room's shape and contents. The larger the
room, the longer the reflection delay times. The early and late reflections'
intensities define the gain (in decibels) of the reflected signals as
compared to the direct signal. These intensities give the listener an
impression of the absorptive nature of the surfaces and objects in the room.
The decay time defines how long the reverberation takes to exponentially
decay until it is no longer perceptible ("effective zero"). The larger and
less absorbent the surfaces, the longer the decay time.

The set of parameters defined here may not include all aspects of
reverberation as specified by some systems. For example, the Midi
Manufacturer's Association (MMA) has an Interactive Audio Special Interest
Group (IASIG), which has a 3-D Working Group that has defined a Level 2 Spec
(I3DL2). I3DL2 supports filtering of reverberation and control of reverb
density. These properties are not included in the JavaSound 1.0 definition of
a reverb control. In such a case, the implementing system should either
extend the defined reverb control to include additional parameters, or else
interpret the system's additional capabilities in a way that fits the model
described here.

If implementing JavaSound on a I3DL2-compliant device:

- Filtering is disabled (high-frequency attenuations are set to 0.0 dB)

Density parameters are set to midway between minimum and maximum

The following table shows what parameter values an implementation might use
for a representative set of reverberation settings.

Reverb types and params: decay time, late intensity, late delay,
early intensity, and early delay

Type

Decay Time (ms)

Late Intensity (dB)

Late Delay (ms)

Early Intensity (dB)

Early Delay(ms)

Cavern

2250

-2.0

41.3

-1.4

10.3

Dungeon

1600

-1.0

10.3

-0.7

2.6

Garage

900

-6.0

14.7

-4.0

3.9

Acoustic Lab

280

-3.0

8.0

-2.0

2.0

Closet

150

-10.0

2.5

-7.0

0.6

**Since:** 1.3

public class

ReverbType

extends

Object

The

ReverbType

class provides methods for accessing various
reverberation settings to be applied to an audio signal.

Reverberation simulates the reflection of sound off of the walls, ceiling,
and floor of a room. Depending on the size of the room, and how absorbent or
reflective the materials in the room's surfaces are, the sound might bounce
around for a long time before dying away.

The reverberation parameters provided by

ReverbType

consist of the
delay time and intensity of early reflections, the delay time and intensity
of late reflections, and an overall decay time. Early reflections are the
initial individual low-order reflections of the direct signal off the
surfaces in the room. The late reflections are the dense, high-order
reflections that characterize the room's reverberation. The delay times for
the start of these two reflection types give the listener a sense of the
overall size and complexity of the room's shape and contents. The larger the
room, the longer the reflection delay times. The early and late reflections'
intensities define the gain (in decibels) of the reflected signals as
compared to the direct signal. These intensities give the listener an
impression of the absorptive nature of the surfaces and objects in the room.
The decay time defines how long the reverberation takes to exponentially
decay until it is no longer perceptible ("effective zero"). The larger and
less absorbent the surfaces, the longer the decay time.

The set of parameters defined here may not include all aspects of
reverberation as specified by some systems. For example, the Midi
Manufacturer's Association (MMA) has an Interactive Audio Special Interest
Group (IASIG), which has a 3-D Working Group that has defined a Level 2 Spec
(I3DL2). I3DL2 supports filtering of reverberation and control of reverb
density. These properties are not included in the JavaSound 1.0 definition of
a reverb control. In such a case, the implementing system should either
extend the defined reverb control to include additional parameters, or else
interpret the system's additional capabilities in a way that fits the model
described here.

If implementing JavaSound on a I3DL2-compliant device:

- Filtering is disabled (high-frequency attenuations are set to 0.0 dB)

Density parameters are set to midway between minimum and maximum

The following table shows what parameter values an implementation might use
for a representative set of reverberation settings.

Reverb types and params: decay time, late intensity, late delay,
early intensity, and early delay

Type

Decay Time (ms)

Late Intensity (dB)

Late Delay (ms)

Early Intensity (dB)

Early Delay(ms)

Cavern

2250

-2.0

41.3

-1.4

10.3

Dungeon

1600

-1.0

10.3

-0.7

2.6

Garage

900

-6.0

14.7

-4.0

3.9

Acoustic Lab

280

-3.0

8.0

-2.0

2.0

Closet

150

-10.0

2.5

-7.0

0.6

Reverberation simulates the reflection of sound off of the walls, ceiling,
and floor of a room. Depending on the size of the room, and how absorbent or
reflective the materials in the room's surfaces are, the sound might bounce
around for a long time before dying away.

The reverberation parameters provided by

ReverbType

consist of the
delay time and intensity of early reflections, the delay time and intensity
of late reflections, and an overall decay time. Early reflections are the
initial individual low-order reflections of the direct signal off the
surfaces in the room. The late reflections are the dense, high-order
reflections that characterize the room's reverberation. The delay times for
the start of these two reflection types give the listener a sense of the
overall size and complexity of the room's shape and contents. The larger the
room, the longer the reflection delay times. The early and late reflections'
intensities define the gain (in decibels) of the reflected signals as
compared to the direct signal. These intensities give the listener an
impression of the absorptive nature of the surfaces and objects in the room.
The decay time defines how long the reverberation takes to exponentially
decay until it is no longer perceptible ("effective zero"). The larger and
less absorbent the surfaces, the longer the decay time.

The set of parameters defined here may not include all aspects of
reverberation as specified by some systems. For example, the Midi
Manufacturer's Association (MMA) has an Interactive Audio Special Interest
Group (IASIG), which has a 3-D Working Group that has defined a Level 2 Spec
(I3DL2). I3DL2 supports filtering of reverberation and control of reverb
density. These properties are not included in the JavaSound 1.0 definition of
a reverb control. In such a case, the implementing system should either
extend the defined reverb control to include additional parameters, or else
interpret the system's additional capabilities in a way that fits the model
described here.

If implementing JavaSound on a I3DL2-compliant device:

- Filtering is disabled (high-frequency attenuations are set to 0.0 dB)

Density parameters are set to midway between minimum and maximum

The following table shows what parameter values an implementation might use
for a representative set of reverberation settings.

Reverb types and params: decay time, late intensity, late delay,
early intensity, and early delay

Type

Decay Time (ms)

Late Intensity (dB)

Late Delay (ms)

Early Intensity (dB)

Early Delay(ms)

Cavern

2250

-2.0

41.3

-1.4

10.3

Dungeon

1600

-1.0

10.3

-0.7

2.6

Garage

900

-6.0

14.7

-4.0

3.9

Acoustic Lab

280

-3.0

8.0

-2.0

2.0

Closet

150

-10.0

2.5

-7.0

0.6

The reverberation parameters provided by

ReverbType

consist of the
delay time and intensity of early reflections, the delay time and intensity
of late reflections, and an overall decay time. Early reflections are the
initial individual low-order reflections of the direct signal off the
surfaces in the room. The late reflections are the dense, high-order
reflections that characterize the room's reverberation. The delay times for
the start of these two reflection types give the listener a sense of the
overall size and complexity of the room's shape and contents. The larger the
room, the longer the reflection delay times. The early and late reflections'
intensities define the gain (in decibels) of the reflected signals as
compared to the direct signal. These intensities give the listener an
impression of the absorptive nature of the surfaces and objects in the room.
The decay time defines how long the reverberation takes to exponentially
decay until it is no longer perceptible ("effective zero"). The larger and
less absorbent the surfaces, the longer the decay time.

The set of parameters defined here may not include all aspects of
reverberation as specified by some systems. For example, the Midi
Manufacturer's Association (MMA) has an Interactive Audio Special Interest
Group (IASIG), which has a 3-D Working Group that has defined a Level 2 Spec
(I3DL2). I3DL2 supports filtering of reverberation and control of reverb
density. These properties are not included in the JavaSound 1.0 definition of
a reverb control. In such a case, the implementing system should either
extend the defined reverb control to include additional parameters, or else
interpret the system's additional capabilities in a way that fits the model
described here.

If implementing JavaSound on a I3DL2-compliant device:

- Filtering is disabled (high-frequency attenuations are set to 0.0 dB)

Density parameters are set to midway between minimum and maximum

The following table shows what parameter values an implementation might use
for a representative set of reverberation settings.

Reverb types and params: decay time, late intensity, late delay,
early intensity, and early delay

Type

Decay Time (ms)

Late Intensity (dB)

Late Delay (ms)

Early Intensity (dB)

Early Delay(ms)

Cavern

2250

-2.0

41.3

-1.4

10.3

Dungeon

1600

-1.0

10.3

-0.7

2.6

Garage

900

-6.0

14.7

-4.0

3.9

Acoustic Lab

280

-3.0

8.0

-2.0

2.0

Closet

150

-10.0

2.5

-7.0

0.6

The set of parameters defined here may not include all aspects of
reverberation as specified by some systems. For example, the Midi
Manufacturer's Association (MMA) has an Interactive Audio Special Interest
Group (IASIG), which has a 3-D Working Group that has defined a Level 2 Spec
(I3DL2). I3DL2 supports filtering of reverberation and control of reverb
density. These properties are not included in the JavaSound 1.0 definition of
a reverb control. In such a case, the implementing system should either
extend the defined reverb control to include additional parameters, or else
interpret the system's additional capabilities in a way that fits the model
described here.

If implementing JavaSound on a I3DL2-compliant device:

- Filtering is disabled (high-frequency attenuations are set to 0.0 dB)

Density parameters are set to midway between minimum and maximum

The following table shows what parameter values an implementation might use
for a representative set of reverberation settings.

Reverb types and params: decay time, late intensity, late delay,
early intensity, and early delay

Type

Decay Time (ms)

Late Intensity (dB)

Late Delay (ms)

Early Intensity (dB)

Early Delay(ms)

Cavern

2250

-2.0

41.3

-1.4

10.3

Dungeon

1600

-1.0

10.3

-0.7

2.6

Garage

900

-6.0

14.7

-4.0

3.9

Acoustic Lab

280

-3.0

8.0

-2.0

2.0

Closet

150

-10.0

2.5

-7.0

0.6

If implementing JavaSound on a I3DL2-compliant device:

- Filtering is disabled (high-frequency attenuations are set to 0.0 dB)

Density parameters are set to midway between minimum and maximum

The following table shows what parameter values an implementation might use
for a representative set of reverberation settings.

Reverb types and params: decay time, late intensity, late delay,
early intensity, and early delay

Type

Decay Time (ms)

Late Intensity (dB)

Late Delay (ms)

Early Intensity (dB)

Early Delay(ms)

Cavern

2250

-2.0

41.3

-1.4

10.3

Dungeon

1600

-1.0

10.3

-0.7

2.6

Garage

900

-6.0

14.7

-4.0

3.9

Acoustic Lab

280

-3.0

8.0

-2.0

2.0

Closet

150

-10.0

2.5

-7.0

0.6

Filtering is disabled (high-frequency attenuations are set to 0.0 dB)

Density parameters are set to midway between minimum and maximum

The following table shows what parameter values an implementation might use
for a representative set of reverberation settings.

Reverb types and params: decay time, late intensity, late delay,
early intensity, and early delay

Type

Decay Time (ms)

Late Intensity (dB)

Late Delay (ms)

Early Intensity (dB)

Early Delay(ms)

Cavern

2250

-2.0

41.3

-1.4

10.3

Dungeon

1600

-1.0

10.3

-0.7

2.6

Garage

900

-6.0

14.7

-4.0

3.9

Acoustic Lab

280

-3.0

8.0

-2.0

2.0

Closet

150

-10.0

2.5

-7.0

0.6

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ReverbType

​(

String

name,
int earlyReflectionDelay,
float earlyReflectionIntensity,
int lateReflectionDelay,
float lateReflectionIntensity,
int decayTime)

Constructs a new reverb type that has the specified reverberation
parameter values.

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

Indicates whether the specified object is equal to this reverb type,
returning

true

if the objects are the same.

int

getDecayTime

()

Obtains the decay time, which is the amount of time over which the late
reflections attenuate to effective zero.

int

getEarlyReflectionDelay

()

Returns the early reflection delay time in microseconds.

float

getEarlyReflectionIntensity

()

Returns the early reflection intensity in decibels.

int

getLateReflectionDelay

()

Returns the late reflection delay time in microseconds.

float

getLateReflectionIntensity

()

Returns the late reflection intensity in decibels.

String

getName

()

Obtains the name of this reverb type.

int

hashCode

()

Returns a hash code value for this reverb type.

String

toString

()

Provides a

String

representation of the reverb type, including
its name and its parameter settings.

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ReverbType

​(

String

name,
int earlyReflectionDelay,
float earlyReflectionIntensity,
int lateReflectionDelay,
float lateReflectionIntensity,
int decayTime)

Constructs a new reverb type that has the specified reverberation
parameter values.

---

#### Constructor Summary

Constructs a new reverb type that has the specified reverberation
parameter values.

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

Indicates whether the specified object is equal to this reverb type,
returning

true

if the objects are the same.

int

getDecayTime

()

Obtains the decay time, which is the amount of time over which the late
reflections attenuate to effective zero.

int

getEarlyReflectionDelay

()

Returns the early reflection delay time in microseconds.

float

getEarlyReflectionIntensity

()

Returns the early reflection intensity in decibels.

int

getLateReflectionDelay

()

Returns the late reflection delay time in microseconds.

float

getLateReflectionIntensity

()

Returns the late reflection intensity in decibels.

String

getName

()

Obtains the name of this reverb type.

int

hashCode

()

Returns a hash code value for this reverb type.

String

toString

()

Provides a

String

representation of the reverb type, including
its name and its parameter settings.

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

Indicates whether the specified object is equal to this reverb type,
returning

true

if the objects are the same.

Obtains the decay time, which is the amount of time over which the late
reflections attenuate to effective zero.

Returns the early reflection delay time in microseconds.

Returns the early reflection intensity in decibels.

Returns the late reflection delay time in microseconds.

Returns the late reflection intensity in decibels.

Obtains the name of this reverb type.

Returns a hash code value for this reverb type.

Provides a

String

representation of the reverb type, including
its name and its parameter settings.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ReverbType

```java
protected ReverbType​(
String
name,
int earlyReflectionDelay,
float earlyReflectionIntensity,
int lateReflectionDelay,
float lateReflectionIntensity,
int decayTime)
```

Constructs a new reverb type that has the specified reverberation
parameter values.

**Parameters:** name

- the name of the new reverb type, or a zero-length

String
**Parameters:** earlyReflectionDelay

- the new type's early reflection delay time
in microseconds
**Parameters:** earlyReflectionIntensity

- the new type's early reflection
intensity in dB
**Parameters:** lateReflectionDelay

- the new type's late reflection delay time in
microseconds
**Parameters:** lateReflectionIntensity

- the new type's late reflection intensity
in dB
**Parameters:** decayTime

- the new type's decay time in microseconds

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Obtains the name of this reverb type.

**Returns:** the name of this reverb type
**Since:** 1.5

- getEarlyReflectionDelay

```java
public final int getEarlyReflectionDelay()
```

Returns the early reflection delay time in microseconds. This is the
amount of time between when the direct signal is heard and when the first
early reflections are heard.

**Returns:** early reflection delay time for this reverb type, in microseconds

- getEarlyReflectionIntensity

```java
public final float getEarlyReflectionIntensity()
```

Returns the early reflection intensity in decibels. This is the amplitude
attenuation of the first early reflections relative to the direct signal.

**Returns:** early reflection intensity for this reverb type, in dB

- getLateReflectionDelay

```java
public final int getLateReflectionDelay()
```

Returns the late reflection delay time in microseconds. This is the
amount of time between when the first early reflections are heard and
when the first late reflections are heard.

**Returns:** late reflection delay time for this reverb type, in microseconds

- getLateReflectionIntensity

```java
public final float getLateReflectionIntensity()
```

Returns the late reflection intensity in decibels. This is the amplitude
attenuation of the first late reflections relative to the direct signal.

**Returns:** late reflection intensity for this reverb type, in dB

- getDecayTime

```java
public final int getDecayTime()
```

Obtains the decay time, which is the amount of time over which the late
reflections attenuate to effective zero. The effective zero value is
implementation-dependent.

**Returns:** the decay time of the late reflections, in microseconds

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this reverb type,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this reverb
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this reverb type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this reverb type
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

representation of the reverb type, including
its name and its parameter settings. The exact contents of the string may
vary between implementations of Java Sound.

**Overrides:** toString

in class

Object
**Returns:** reverberation type name and description

Constructor Detail

- ReverbType

```java
protected ReverbType​(
String
name,
int earlyReflectionDelay,
float earlyReflectionIntensity,
int lateReflectionDelay,
float lateReflectionIntensity,
int decayTime)
```

Constructs a new reverb type that has the specified reverberation
parameter values.

**Parameters:** name

- the name of the new reverb type, or a zero-length

String
**Parameters:** earlyReflectionDelay

- the new type's early reflection delay time
in microseconds
**Parameters:** earlyReflectionIntensity

- the new type's early reflection
intensity in dB
**Parameters:** lateReflectionDelay

- the new type's late reflection delay time in
microseconds
**Parameters:** lateReflectionIntensity

- the new type's late reflection intensity
in dB
**Parameters:** decayTime

- the new type's decay time in microseconds

---

#### Constructor Detail

ReverbType

```java
protected ReverbType​(
String
name,
int earlyReflectionDelay,
float earlyReflectionIntensity,
int lateReflectionDelay,
float lateReflectionIntensity,
int decayTime)
```

Constructs a new reverb type that has the specified reverberation
parameter values.

**Parameters:** name

- the name of the new reverb type, or a zero-length

String
**Parameters:** earlyReflectionDelay

- the new type's early reflection delay time
in microseconds
**Parameters:** earlyReflectionIntensity

- the new type's early reflection
intensity in dB
**Parameters:** lateReflectionDelay

- the new type's late reflection delay time in
microseconds
**Parameters:** lateReflectionIntensity

- the new type's late reflection intensity
in dB
**Parameters:** decayTime

- the new type's decay time in microseconds

---

#### ReverbType

protected ReverbType​(

String

name,
int earlyReflectionDelay,
float earlyReflectionIntensity,
int lateReflectionDelay,
float lateReflectionIntensity,
int decayTime)

Constructs a new reverb type that has the specified reverberation
parameter values.

Method Detail

- getName

```java
public
String
getName()
```

Obtains the name of this reverb type.

**Returns:** the name of this reverb type
**Since:** 1.5

- getEarlyReflectionDelay

```java
public final int getEarlyReflectionDelay()
```

Returns the early reflection delay time in microseconds. This is the
amount of time between when the direct signal is heard and when the first
early reflections are heard.

**Returns:** early reflection delay time for this reverb type, in microseconds

- getEarlyReflectionIntensity

```java
public final float getEarlyReflectionIntensity()
```

Returns the early reflection intensity in decibels. This is the amplitude
attenuation of the first early reflections relative to the direct signal.

**Returns:** early reflection intensity for this reverb type, in dB

- getLateReflectionDelay

```java
public final int getLateReflectionDelay()
```

Returns the late reflection delay time in microseconds. This is the
amount of time between when the first early reflections are heard and
when the first late reflections are heard.

**Returns:** late reflection delay time for this reverb type, in microseconds

- getLateReflectionIntensity

```java
public final float getLateReflectionIntensity()
```

Returns the late reflection intensity in decibels. This is the amplitude
attenuation of the first late reflections relative to the direct signal.

**Returns:** late reflection intensity for this reverb type, in dB

- getDecayTime

```java
public final int getDecayTime()
```

Obtains the decay time, which is the amount of time over which the late
reflections attenuate to effective zero. The effective zero value is
implementation-dependent.

**Returns:** the decay time of the late reflections, in microseconds

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this reverb type,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this reverb
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this reverb type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this reverb type
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

representation of the reverb type, including
its name and its parameter settings. The exact contents of the string may
vary between implementations of Java Sound.

**Overrides:** toString

in class

Object
**Returns:** reverberation type name and description

---

#### Method Detail

getName

```java
public
String
getName()
```

Obtains the name of this reverb type.

**Returns:** the name of this reverb type
**Since:** 1.5

---

#### getName

public

String

getName()

Obtains the name of this reverb type.

getEarlyReflectionDelay

```java
public final int getEarlyReflectionDelay()
```

Returns the early reflection delay time in microseconds. This is the
amount of time between when the direct signal is heard and when the first
early reflections are heard.

**Returns:** early reflection delay time for this reverb type, in microseconds

---

#### getEarlyReflectionDelay

public final int getEarlyReflectionDelay()

Returns the early reflection delay time in microseconds. This is the
amount of time between when the direct signal is heard and when the first
early reflections are heard.

getEarlyReflectionIntensity

```java
public final float getEarlyReflectionIntensity()
```

Returns the early reflection intensity in decibels. This is the amplitude
attenuation of the first early reflections relative to the direct signal.

**Returns:** early reflection intensity for this reverb type, in dB

---

#### getEarlyReflectionIntensity

public final float getEarlyReflectionIntensity()

Returns the early reflection intensity in decibels. This is the amplitude
attenuation of the first early reflections relative to the direct signal.

getLateReflectionDelay

```java
public final int getLateReflectionDelay()
```

Returns the late reflection delay time in microseconds. This is the
amount of time between when the first early reflections are heard and
when the first late reflections are heard.

**Returns:** late reflection delay time for this reverb type, in microseconds

---

#### getLateReflectionDelay

public final int getLateReflectionDelay()

Returns the late reflection delay time in microseconds. This is the
amount of time between when the first early reflections are heard and
when the first late reflections are heard.

getLateReflectionIntensity

```java
public final float getLateReflectionIntensity()
```

Returns the late reflection intensity in decibels. This is the amplitude
attenuation of the first late reflections relative to the direct signal.

**Returns:** late reflection intensity for this reverb type, in dB

---

#### getLateReflectionIntensity

public final float getLateReflectionIntensity()

Returns the late reflection intensity in decibels. This is the amplitude
attenuation of the first late reflections relative to the direct signal.

getDecayTime

```java
public final int getDecayTime()
```

Obtains the decay time, which is the amount of time over which the late
reflections attenuate to effective zero. The effective zero value is
implementation-dependent.

**Returns:** the decay time of the late reflections, in microseconds

---

#### getDecayTime

public final int getDecayTime()

Obtains the decay time, which is the amount of time over which the late
reflections attenuate to effective zero. The effective zero value is
implementation-dependent.

equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this reverb type,
returning

true

if the objects are the same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this reverb
type;

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

Indicates whether the specified object is equal to this reverb type,
returning

true

if the objects are the same.

hashCode

```java
public final int hashCode()
```

Returns a hash code value for this reverb type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this reverb type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hash code value for this reverb type.

toString

```java
public final
String
toString()
```

Provides a

String

representation of the reverb type, including
its name and its parameter settings. The exact contents of the string may
vary between implementations of Java Sound.

**Overrides:** toString

in class

Object
**Returns:** reverberation type name and description

---

#### toString

public final

String

toString()

Provides a

String

representation of the reverb type, including
its name and its parameter settings. The exact contents of the string may
vary between implementations of Java Sound.

---

