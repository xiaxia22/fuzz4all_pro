# Class FloatControl.Type

**Source:** `java.desktop\javax\sound\sampled\FloatControl.Type.html`

### Class Description

```java
public static class
FloatControl.Type

extends
Control.Type
```

An instance of the

FloatControl.Type

inner class identifies one
kind of float control. Static instances are provided for the common
types.

**Enclosing class:** FloatControl

---

### Field Details

#### public static final
FloatControl.Type
MASTER_GAIN

Represents a control for the overall gain on a line.

Gain is a quantity in decibels (dB) that is added to the intrinsic
decibel level of the audio signal--that is, the level of the signal
before it is altered by the gain control. A positive gain amplifies
(boosts) the signal's volume, and a negative gain attenuates(cuts)it.
The gain setting defaults to a value of 0.0 dB, meaning the signal's
loudness is unaffected. Note that gain measures dB, not amplitude.
The relationship between a gain in decibels and the corresponding
linear amplitude multiplier is:

linearScalar = pow(10.0, gainDB/20.0)

The

FloatControl

class has methods to impose a maximum and
minimum allowable value for gain. However, because an audio signal
might already be at a high amplitude, the maximum setting does not
guarantee that the signal will be undistorted when the gain is
applied to it (unless the maximum is zero or negative). To avoid
numeric overflow from excessively large gain settings, a gain control
can implement clipping, meaning that the signal's amplitude will be
limited to the maximum value representable by its audio format,
instead of wrapping around.

These comments apply to gain controls in general, not just master
gain controls. A line can have more than one gain control. For
example, a mixer (which is itself a line) might have a master gain
control, an auxiliary return control, a reverb return control, and,
on each of its source lines, an individual aux send and reverb send.

**See Also:**
- AUX_SEND

,

AUX_RETURN

,

REVERB_SEND

,

REVERB_RETURN

,

VOLUME

---

#### public static final
FloatControl.Type
AUX_SEND

Represents a control for the auxiliary send gain on a line.

**See Also:**
- MASTER_GAIN

,

AUX_RETURN

---

#### public static final
FloatControl.Type
AUX_RETURN

Represents a control for the auxiliary return gain on a line.

**See Also:**
- MASTER_GAIN

,

AUX_SEND

---

#### public static final
FloatControl.Type
REVERB_SEND

Represents a control for the pre-reverb gain on a line. This control
may be used to affect how much of a line's signal is directed to a
mixer's internal reverberation unit.

**See Also:**
- MASTER_GAIN

,

REVERB_RETURN

,

EnumControl.Type.REVERB

---

#### public static final
FloatControl.Type
REVERB_RETURN

Represents a control for the post-reverb gain on a line. This control
may be used to control the relative amplitude of the signal returned
from an internal reverberation unit.

**See Also:**
- MASTER_GAIN

,

REVERB_SEND

---

#### public static final
FloatControl.Type
VOLUME

Represents a control for the volume on a line.

---

#### public static final
FloatControl.Type
PAN

Represents a control for the relative pan (left-right positioning) of
the signal. The signal may be mono; the pan setting affects how it is
distributed by the mixer in a stereo mix. The valid range of values
is -1.0 (left channel only) to 1.0 (right channel only). The default
is 0.0 (centered).

**See Also:**
- BALANCE

---

#### public static final
FloatControl.Type
BALANCE

Represents a control for the relative balance of a stereo signal
between two stereo speakers. The valid range of values is -1.0 (left
channel only) to 1.0 (right channel only). The default is 0.0
(centered).

**See Also:**
- PAN

---

#### public static final
FloatControl.Type
SAMPLE_RATE

Represents a control that changes the sample rate of audio playback.
The net effect of changing the sample rate depends on the
relationship between the media's natural rate and the rate that is
set via this control. The natural rate is the sample rate that is
specified in the data line's

AudioFormat

object. For example,
if the natural rate of the media is 11025 samples per second and the
sample rate is set to 22050 samples per second, the media will play
back at twice the normal speed.

Changing the sample rate with this control does not affect the data
line's audio format. Also note that whenever you change a sound's
sample rate, a change in the sound's pitch results. For example,
doubling the sample rate has the effect of doubling the frequencies
in the sound's spectrum, which raises the pitch by an octave.

---

### Constructor Details

#### protected Type​(
String
name)

Constructs a new float control type.

**Parameters:**
- name

- the name of the new float control type

---

### Method Details

*No entries found.*

### Additional Sections

#### Class FloatControl.Type

java.lang.Object

- javax.sound.sampled.Control.Type
- - javax.sound.sampled.FloatControl.Type

javax.sound.sampled.Control.Type

- javax.sound.sampled.FloatControl.Type

javax.sound.sampled.FloatControl.Type

**Enclosing class:** FloatControl

```java
public static class
FloatControl.Type

extends
Control.Type
```

An instance of the

FloatControl.Type

inner class identifies one
kind of float control. Static instances are provided for the common
types.

**Since:** 1.3

public static class

FloatControl.Type

extends

Control.Type

An instance of the

FloatControl.Type

inner class identifies one
kind of float control. Static instances are provided for the common
types.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

FloatControl.Type

AUX_RETURN

Represents a control for the auxiliary return gain on a line.

static

FloatControl.Type

AUX_SEND

Represents a control for the auxiliary send gain on a line.

static

FloatControl.Type

BALANCE

Represents a control for the relative balance of a stereo signal
between two stereo speakers.

static

FloatControl.Type

MASTER_GAIN

Represents a control for the overall gain on a line.

static

FloatControl.Type

PAN

Represents a control for the relative pan (left-right positioning) of
the signal.

static

FloatControl.Type

REVERB_RETURN

Represents a control for the post-reverb gain on a line.

static

FloatControl.Type

REVERB_SEND

Represents a control for the pre-reverb gain on a line.

static

FloatControl.Type

SAMPLE_RATE

Represents a control that changes the sample rate of audio playback.

static

FloatControl.Type

VOLUME

Represents a control for the volume on a line.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Type

​(

String

name)

Constructs a new float control type.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.sound.sampled.

Control.Type

equals

,

hashCode

,

toString

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

FloatControl.Type

AUX_RETURN

Represents a control for the auxiliary return gain on a line.

static

FloatControl.Type

AUX_SEND

Represents a control for the auxiliary send gain on a line.

static

FloatControl.Type

BALANCE

Represents a control for the relative balance of a stereo signal
between two stereo speakers.

static

FloatControl.Type

MASTER_GAIN

Represents a control for the overall gain on a line.

static

FloatControl.Type

PAN

Represents a control for the relative pan (left-right positioning) of
the signal.

static

FloatControl.Type

REVERB_RETURN

Represents a control for the post-reverb gain on a line.

static

FloatControl.Type

REVERB_SEND

Represents a control for the pre-reverb gain on a line.

static

FloatControl.Type

SAMPLE_RATE

Represents a control that changes the sample rate of audio playback.

static

FloatControl.Type

VOLUME

Represents a control for the volume on a line.

---

#### Field Summary

Represents a control for the auxiliary return gain on a line.

Represents a control for the auxiliary send gain on a line.

Represents a control for the relative balance of a stereo signal
between two stereo speakers.

Represents a control for the overall gain on a line.

Represents a control for the relative pan (left-right positioning) of
the signal.

Represents a control for the post-reverb gain on a line.

Represents a control for the pre-reverb gain on a line.

Represents a control that changes the sample rate of audio playback.

Represents a control for the volume on a line.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Type

​(

String

name)

Constructs a new float control type.

---

#### Constructor Summary

Constructs a new float control type.

Method Summary

- Methods declared in class javax.sound.sampled.

Control.Type

equals

,

hashCode

,

toString

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

Methods declared in class javax.sound.sampled.

Control.Type

equals

,

hashCode

,

toString

---

#### Methods declared in class javax.sound.sampled. Control.Type

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

- MASTER_GAIN

```java
public static final
FloatControl.Type
MASTER_GAIN
```

Represents a control for the overall gain on a line.

Gain is a quantity in decibels (dB) that is added to the intrinsic
decibel level of the audio signal--that is, the level of the signal
before it is altered by the gain control. A positive gain amplifies
(boosts) the signal's volume, and a negative gain attenuates(cuts)it.
The gain setting defaults to a value of 0.0 dB, meaning the signal's
loudness is unaffected. Note that gain measures dB, not amplitude.
The relationship between a gain in decibels and the corresponding
linear amplitude multiplier is:

linearScalar = pow(10.0, gainDB/20.0)

The

FloatControl

class has methods to impose a maximum and
minimum allowable value for gain. However, because an audio signal
might already be at a high amplitude, the maximum setting does not
guarantee that the signal will be undistorted when the gain is
applied to it (unless the maximum is zero or negative). To avoid
numeric overflow from excessively large gain settings, a gain control
can implement clipping, meaning that the signal's amplitude will be
limited to the maximum value representable by its audio format,
instead of wrapping around.

These comments apply to gain controls in general, not just master
gain controls. A line can have more than one gain control. For
example, a mixer (which is itself a line) might have a master gain
control, an auxiliary return control, a reverb return control, and,
on each of its source lines, an individual aux send and reverb send.

**See Also:** AUX_SEND

,

AUX_RETURN

,

REVERB_SEND

,

REVERB_RETURN

,

VOLUME

- AUX_SEND

```java
public static final
FloatControl.Type
AUX_SEND
```

Represents a control for the auxiliary send gain on a line.

**See Also:** MASTER_GAIN

,

AUX_RETURN

- AUX_RETURN

```java
public static final
FloatControl.Type
AUX_RETURN
```

Represents a control for the auxiliary return gain on a line.

**See Also:** MASTER_GAIN

,

AUX_SEND

- REVERB_SEND

```java
public static final
FloatControl.Type
REVERB_SEND
```

Represents a control for the pre-reverb gain on a line. This control
may be used to affect how much of a line's signal is directed to a
mixer's internal reverberation unit.

**See Also:** MASTER_GAIN

,

REVERB_RETURN

,

EnumControl.Type.REVERB

- REVERB_RETURN

```java
public static final
FloatControl.Type
REVERB_RETURN
```

Represents a control for the post-reverb gain on a line. This control
may be used to control the relative amplitude of the signal returned
from an internal reverberation unit.

**See Also:** MASTER_GAIN

,

REVERB_SEND

- VOLUME

```java
public static final
FloatControl.Type
VOLUME
```

Represents a control for the volume on a line.

- PAN

```java
public static final
FloatControl.Type
PAN
```

Represents a control for the relative pan (left-right positioning) of
the signal. The signal may be mono; the pan setting affects how it is
distributed by the mixer in a stereo mix. The valid range of values
is -1.0 (left channel only) to 1.0 (right channel only). The default
is 0.0 (centered).

**See Also:** BALANCE

- BALANCE

```java
public static final
FloatControl.Type
BALANCE
```

Represents a control for the relative balance of a stereo signal
between two stereo speakers. The valid range of values is -1.0 (left
channel only) to 1.0 (right channel only). The default is 0.0
(centered).

**See Also:** PAN

- SAMPLE_RATE

```java
public static final
FloatControl.Type
SAMPLE_RATE
```

Represents a control that changes the sample rate of audio playback.
The net effect of changing the sample rate depends on the
relationship between the media's natural rate and the rate that is
set via this control. The natural rate is the sample rate that is
specified in the data line's

AudioFormat

object. For example,
if the natural rate of the media is 11025 samples per second and the
sample rate is set to 22050 samples per second, the media will play
back at twice the normal speed.

Changing the sample rate with this control does not affect the data
line's audio format. Also note that whenever you change a sound's
sample rate, a change in the sound's pitch results. For example,
doubling the sample rate has the effect of doubling the frequencies
in the sound's spectrum, which raises the pitch by an octave.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Type

```java
protected Type​(
String
name)
```

Constructs a new float control type.

**Parameters:** name

- the name of the new float control type

Field Detail

- MASTER_GAIN

```java
public static final
FloatControl.Type
MASTER_GAIN
```

Represents a control for the overall gain on a line.

Gain is a quantity in decibels (dB) that is added to the intrinsic
decibel level of the audio signal--that is, the level of the signal
before it is altered by the gain control. A positive gain amplifies
(boosts) the signal's volume, and a negative gain attenuates(cuts)it.
The gain setting defaults to a value of 0.0 dB, meaning the signal's
loudness is unaffected. Note that gain measures dB, not amplitude.
The relationship between a gain in decibels and the corresponding
linear amplitude multiplier is:

linearScalar = pow(10.0, gainDB/20.0)

The

FloatControl

class has methods to impose a maximum and
minimum allowable value for gain. However, because an audio signal
might already be at a high amplitude, the maximum setting does not
guarantee that the signal will be undistorted when the gain is
applied to it (unless the maximum is zero or negative). To avoid
numeric overflow from excessively large gain settings, a gain control
can implement clipping, meaning that the signal's amplitude will be
limited to the maximum value representable by its audio format,
instead of wrapping around.

These comments apply to gain controls in general, not just master
gain controls. A line can have more than one gain control. For
example, a mixer (which is itself a line) might have a master gain
control, an auxiliary return control, a reverb return control, and,
on each of its source lines, an individual aux send and reverb send.

**See Also:** AUX_SEND

,

AUX_RETURN

,

REVERB_SEND

,

REVERB_RETURN

,

VOLUME

- AUX_SEND

```java
public static final
FloatControl.Type
AUX_SEND
```

Represents a control for the auxiliary send gain on a line.

**See Also:** MASTER_GAIN

,

AUX_RETURN

- AUX_RETURN

```java
public static final
FloatControl.Type
AUX_RETURN
```

Represents a control for the auxiliary return gain on a line.

**See Also:** MASTER_GAIN

,

AUX_SEND

- REVERB_SEND

```java
public static final
FloatControl.Type
REVERB_SEND
```

Represents a control for the pre-reverb gain on a line. This control
may be used to affect how much of a line's signal is directed to a
mixer's internal reverberation unit.

**See Also:** MASTER_GAIN

,

REVERB_RETURN

,

EnumControl.Type.REVERB

- REVERB_RETURN

```java
public static final
FloatControl.Type
REVERB_RETURN
```

Represents a control for the post-reverb gain on a line. This control
may be used to control the relative amplitude of the signal returned
from an internal reverberation unit.

**See Also:** MASTER_GAIN

,

REVERB_SEND

- VOLUME

```java
public static final
FloatControl.Type
VOLUME
```

Represents a control for the volume on a line.

- PAN

```java
public static final
FloatControl.Type
PAN
```

Represents a control for the relative pan (left-right positioning) of
the signal. The signal may be mono; the pan setting affects how it is
distributed by the mixer in a stereo mix. The valid range of values
is -1.0 (left channel only) to 1.0 (right channel only). The default
is 0.0 (centered).

**See Also:** BALANCE

- BALANCE

```java
public static final
FloatControl.Type
BALANCE
```

Represents a control for the relative balance of a stereo signal
between two stereo speakers. The valid range of values is -1.0 (left
channel only) to 1.0 (right channel only). The default is 0.0
(centered).

**See Also:** PAN

- SAMPLE_RATE

```java
public static final
FloatControl.Type
SAMPLE_RATE
```

Represents a control that changes the sample rate of audio playback.
The net effect of changing the sample rate depends on the
relationship between the media's natural rate and the rate that is
set via this control. The natural rate is the sample rate that is
specified in the data line's

AudioFormat

object. For example,
if the natural rate of the media is 11025 samples per second and the
sample rate is set to 22050 samples per second, the media will play
back at twice the normal speed.

Changing the sample rate with this control does not affect the data
line's audio format. Also note that whenever you change a sound's
sample rate, a change in the sound's pitch results. For example,
doubling the sample rate has the effect of doubling the frequencies
in the sound's spectrum, which raises the pitch by an octave.

---

#### Field Detail

MASTER_GAIN

```java
public static final
FloatControl.Type
MASTER_GAIN
```

Represents a control for the overall gain on a line.

Gain is a quantity in decibels (dB) that is added to the intrinsic
decibel level of the audio signal--that is, the level of the signal
before it is altered by the gain control. A positive gain amplifies
(boosts) the signal's volume, and a negative gain attenuates(cuts)it.
The gain setting defaults to a value of 0.0 dB, meaning the signal's
loudness is unaffected. Note that gain measures dB, not amplitude.
The relationship between a gain in decibels and the corresponding
linear amplitude multiplier is:

linearScalar = pow(10.0, gainDB/20.0)

The

FloatControl

class has methods to impose a maximum and
minimum allowable value for gain. However, because an audio signal
might already be at a high amplitude, the maximum setting does not
guarantee that the signal will be undistorted when the gain is
applied to it (unless the maximum is zero or negative). To avoid
numeric overflow from excessively large gain settings, a gain control
can implement clipping, meaning that the signal's amplitude will be
limited to the maximum value representable by its audio format,
instead of wrapping around.

These comments apply to gain controls in general, not just master
gain controls. A line can have more than one gain control. For
example, a mixer (which is itself a line) might have a master gain
control, an auxiliary return control, a reverb return control, and,
on each of its source lines, an individual aux send and reverb send.

**See Also:** AUX_SEND

,

AUX_RETURN

,

REVERB_SEND

,

REVERB_RETURN

,

VOLUME

---

#### MASTER_GAIN

public static final

FloatControl.Type

MASTER_GAIN

Represents a control for the overall gain on a line.

Gain is a quantity in decibels (dB) that is added to the intrinsic
decibel level of the audio signal--that is, the level of the signal
before it is altered by the gain control. A positive gain amplifies
(boosts) the signal's volume, and a negative gain attenuates(cuts)it.
The gain setting defaults to a value of 0.0 dB, meaning the signal's
loudness is unaffected. Note that gain measures dB, not amplitude.
The relationship between a gain in decibels and the corresponding
linear amplitude multiplier is:

linearScalar = pow(10.0, gainDB/20.0)

The

FloatControl

class has methods to impose a maximum and
minimum allowable value for gain. However, because an audio signal
might already be at a high amplitude, the maximum setting does not
guarantee that the signal will be undistorted when the gain is
applied to it (unless the maximum is zero or negative). To avoid
numeric overflow from excessively large gain settings, a gain control
can implement clipping, meaning that the signal's amplitude will be
limited to the maximum value representable by its audio format,
instead of wrapping around.

These comments apply to gain controls in general, not just master
gain controls. A line can have more than one gain control. For
example, a mixer (which is itself a line) might have a master gain
control, an auxiliary return control, a reverb return control, and,
on each of its source lines, an individual aux send and reverb send.

Gain is a quantity in decibels (dB) that is added to the intrinsic
decibel level of the audio signal--that is, the level of the signal
before it is altered by the gain control. A positive gain amplifies
(boosts) the signal's volume, and a negative gain attenuates(cuts)it.
The gain setting defaults to a value of 0.0 dB, meaning the signal's
loudness is unaffected. Note that gain measures dB, not amplitude.
The relationship between a gain in decibels and the corresponding
linear amplitude multiplier is:

linearScalar = pow(10.0, gainDB/20.0)

The

FloatControl

class has methods to impose a maximum and
minimum allowable value for gain. However, because an audio signal
might already be at a high amplitude, the maximum setting does not
guarantee that the signal will be undistorted when the gain is
applied to it (unless the maximum is zero or negative). To avoid
numeric overflow from excessively large gain settings, a gain control
can implement clipping, meaning that the signal's amplitude will be
limited to the maximum value representable by its audio format,
instead of wrapping around.

These comments apply to gain controls in general, not just master
gain controls. A line can have more than one gain control. For
example, a mixer (which is itself a line) might have a master gain
control, an auxiliary return control, a reverb return control, and,
on each of its source lines, an individual aux send and reverb send.

linearScalar = pow(10.0, gainDB/20.0)

The

FloatControl

class has methods to impose a maximum and
minimum allowable value for gain. However, because an audio signal
might already be at a high amplitude, the maximum setting does not
guarantee that the signal will be undistorted when the gain is
applied to it (unless the maximum is zero or negative). To avoid
numeric overflow from excessively large gain settings, a gain control
can implement clipping, meaning that the signal's amplitude will be
limited to the maximum value representable by its audio format,
instead of wrapping around.

These comments apply to gain controls in general, not just master
gain controls. A line can have more than one gain control. For
example, a mixer (which is itself a line) might have a master gain
control, an auxiliary return control, a reverb return control, and,
on each of its source lines, an individual aux send and reverb send.

The

FloatControl

class has methods to impose a maximum and
minimum allowable value for gain. However, because an audio signal
might already be at a high amplitude, the maximum setting does not
guarantee that the signal will be undistorted when the gain is
applied to it (unless the maximum is zero or negative). To avoid
numeric overflow from excessively large gain settings, a gain control
can implement clipping, meaning that the signal's amplitude will be
limited to the maximum value representable by its audio format,
instead of wrapping around.

These comments apply to gain controls in general, not just master
gain controls. A line can have more than one gain control. For
example, a mixer (which is itself a line) might have a master gain
control, an auxiliary return control, a reverb return control, and,
on each of its source lines, an individual aux send and reverb send.

These comments apply to gain controls in general, not just master
gain controls. A line can have more than one gain control. For
example, a mixer (which is itself a line) might have a master gain
control, an auxiliary return control, a reverb return control, and,
on each of its source lines, an individual aux send and reverb send.

AUX_SEND

```java
public static final
FloatControl.Type
AUX_SEND
```

Represents a control for the auxiliary send gain on a line.

**See Also:** MASTER_GAIN

,

AUX_RETURN

---

#### AUX_SEND

public static final

FloatControl.Type

AUX_SEND

Represents a control for the auxiliary send gain on a line.

AUX_RETURN

```java
public static final
FloatControl.Type
AUX_RETURN
```

Represents a control for the auxiliary return gain on a line.

**See Also:** MASTER_GAIN

,

AUX_SEND

---

#### AUX_RETURN

public static final

FloatControl.Type

AUX_RETURN

Represents a control for the auxiliary return gain on a line.

REVERB_SEND

```java
public static final
FloatControl.Type
REVERB_SEND
```

Represents a control for the pre-reverb gain on a line. This control
may be used to affect how much of a line's signal is directed to a
mixer's internal reverberation unit.

**See Also:** MASTER_GAIN

,

REVERB_RETURN

,

EnumControl.Type.REVERB

---

#### REVERB_SEND

public static final

FloatControl.Type

REVERB_SEND

Represents a control for the pre-reverb gain on a line. This control
may be used to affect how much of a line's signal is directed to a
mixer's internal reverberation unit.

REVERB_RETURN

```java
public static final
FloatControl.Type
REVERB_RETURN
```

Represents a control for the post-reverb gain on a line. This control
may be used to control the relative amplitude of the signal returned
from an internal reverberation unit.

**See Also:** MASTER_GAIN

,

REVERB_SEND

---

#### REVERB_RETURN

public static final

FloatControl.Type

REVERB_RETURN

Represents a control for the post-reverb gain on a line. This control
may be used to control the relative amplitude of the signal returned
from an internal reverberation unit.

VOLUME

```java
public static final
FloatControl.Type
VOLUME
```

Represents a control for the volume on a line.

---

#### VOLUME

public static final

FloatControl.Type

VOLUME

Represents a control for the volume on a line.

PAN

```java
public static final
FloatControl.Type
PAN
```

Represents a control for the relative pan (left-right positioning) of
the signal. The signal may be mono; the pan setting affects how it is
distributed by the mixer in a stereo mix. The valid range of values
is -1.0 (left channel only) to 1.0 (right channel only). The default
is 0.0 (centered).

**See Also:** BALANCE

---

#### PAN

public static final

FloatControl.Type

PAN

Represents a control for the relative pan (left-right positioning) of
the signal. The signal may be mono; the pan setting affects how it is
distributed by the mixer in a stereo mix. The valid range of values
is -1.0 (left channel only) to 1.0 (right channel only). The default
is 0.0 (centered).

BALANCE

```java
public static final
FloatControl.Type
BALANCE
```

Represents a control for the relative balance of a stereo signal
between two stereo speakers. The valid range of values is -1.0 (left
channel only) to 1.0 (right channel only). The default is 0.0
(centered).

**See Also:** PAN

---

#### BALANCE

public static final

FloatControl.Type

BALANCE

Represents a control for the relative balance of a stereo signal
between two stereo speakers. The valid range of values is -1.0 (left
channel only) to 1.0 (right channel only). The default is 0.0
(centered).

SAMPLE_RATE

```java
public static final
FloatControl.Type
SAMPLE_RATE
```

Represents a control that changes the sample rate of audio playback.
The net effect of changing the sample rate depends on the
relationship between the media's natural rate and the rate that is
set via this control. The natural rate is the sample rate that is
specified in the data line's

AudioFormat

object. For example,
if the natural rate of the media is 11025 samples per second and the
sample rate is set to 22050 samples per second, the media will play
back at twice the normal speed.

Changing the sample rate with this control does not affect the data
line's audio format. Also note that whenever you change a sound's
sample rate, a change in the sound's pitch results. For example,
doubling the sample rate has the effect of doubling the frequencies
in the sound's spectrum, which raises the pitch by an octave.

---

#### SAMPLE_RATE

public static final

FloatControl.Type

SAMPLE_RATE

Represents a control that changes the sample rate of audio playback.
The net effect of changing the sample rate depends on the
relationship between the media's natural rate and the rate that is
set via this control. The natural rate is the sample rate that is
specified in the data line's

AudioFormat

object. For example,
if the natural rate of the media is 11025 samples per second and the
sample rate is set to 22050 samples per second, the media will play
back at twice the normal speed.

Changing the sample rate with this control does not affect the data
line's audio format. Also note that whenever you change a sound's
sample rate, a change in the sound's pitch results. For example,
doubling the sample rate has the effect of doubling the frequencies
in the sound's spectrum, which raises the pitch by an octave.

Changing the sample rate with this control does not affect the data
line's audio format. Also note that whenever you change a sound's
sample rate, a change in the sound's pitch results. For example,
doubling the sample rate has the effect of doubling the frequencies
in the sound's spectrum, which raises the pitch by an octave.

Constructor Detail

- Type

```java
protected Type​(
String
name)
```

Constructs a new float control type.

**Parameters:** name

- the name of the new float control type

---

#### Constructor Detail

Type

```java
protected Type​(
String
name)
```

Constructs a new float control type.

**Parameters:** name

- the name of the new float control type

---

#### Type

protected Type​(

String

name)

Constructs a new float control type.

---

