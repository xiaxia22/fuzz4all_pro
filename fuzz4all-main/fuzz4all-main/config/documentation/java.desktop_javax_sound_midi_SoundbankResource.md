# Class SoundbankResource

**Source:** `java.desktop\javax\sound\midi\SoundbankResource.html`

### Class Description

```java
public abstract class
SoundbankResource

extends
Object
```

A

SoundbankResource

represents any audio resource stored in a

Soundbank

. Common soundbank resources include:

- Instruments. An instrument may be specified in a variety of ways.
However, all soundbanks have some mechanism for defining instruments. In
doing so, they may reference other resources stored in the soundbank.
Each instrument has a

Patch

which specifies the MIDI program and
bank by which it may be referenced in MIDI messages. Instrument information
may be stored in

Instrument

objects.

Audio samples. A sample typically is a sampled audio waveform which
contains a short sound recording whose duration is a fraction of a
second, or at most a few seconds. These audio samples may be used by a

Synthesizer

to synthesize sound in response to MIDI commands, or
extracted for use by an application. (The terminology reflects musicians'
use of the word "sample" to refer collectively to a series of contiguous
audio samples or frames, rather than to a single, instantaneous sample.)
The data class for an audio sample will be an object that encapsulates
the audio sample data itself and information about how to interpret it
(the format of the audio data), such as an

AudioInputStream

.

Embedded sequences. A sound bank may contain built-in song data stored
in a data object such as a

Sequence

.

Synthesizers that use wavetable synthesis or related techniques play back the
audio in a sample when synthesizing notes, often when emulating the
real-world instrument that was originally recorded. However, there is not
necessarily a one-to-one correspondence between the

Instruments

and
samples in a

Soundbank

. A single

Instrument

can use multiple
SoundbankResources (typically for notes of dissimilar pitch or brightness).
Also, more than one

Instrument

can use the same sample.

**Direct Known Subclasses:** Instrument

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SoundbankResource​(
Soundbank
soundBank,

String
name,

Class
<?> dataClass)

Constructs a new

SoundbankResource

from the given sound bank and
wavetable index. (Setting the

SoundbankResource's

name, sampled
audio data, and instruments is a subclass responsibility.)

**Parameters:**
- soundBank

- the sound bank containing this

SoundbankResource
- name

- the name of the sample
- dataClass

- the class used to represent the sample's data

**See Also:**
- getSoundbank()

,

getName()

,

getDataClass()

,

getData()

---

### Method Details

#### public
Soundbank
getSoundbank()

Obtains the sound bank that contains this

SoundbankResource

.

**Returns:**
- the sound bank in which this

SoundbankResource

is stored

---

#### public
String
getName()

Obtains the name of the resource. This should generally be a string
descriptive of the resource.

**Returns:**
- the instrument's name

---

#### public
Class
<?> getDataClass()

Obtains the class used by this sample to represent its data. The object
returned by

getData

will be of this class. If this

SoundbankResource

object does not support direct access to its
data, returns

null

.

**Returns:**
- the class used to represent the sample's data, or null if the
data is not accessible

---

#### public abstract
Object
getData()

Obtains the sampled audio that is stored in this

SoundbankResource

. The type of object returned depends on the
implementation of the concrete class, and may be queried using

getDataClass

.

**Returns:**
- an object containing the sampled audio data

**See Also:**
- getDataClass()

---

### Additional Sections

#### Class SoundbankResource

java.lang.Object

- javax.sound.midi.SoundbankResource

javax.sound.midi.SoundbankResource

**Direct Known Subclasses:** Instrument

```java
public abstract class
SoundbankResource

extends
Object
```

A

SoundbankResource

represents any audio resource stored in a

Soundbank

. Common soundbank resources include:

- Instruments. An instrument may be specified in a variety of ways.
However, all soundbanks have some mechanism for defining instruments. In
doing so, they may reference other resources stored in the soundbank.
Each instrument has a

Patch

which specifies the MIDI program and
bank by which it may be referenced in MIDI messages. Instrument information
may be stored in

Instrument

objects.

Audio samples. A sample typically is a sampled audio waveform which
contains a short sound recording whose duration is a fraction of a
second, or at most a few seconds. These audio samples may be used by a

Synthesizer

to synthesize sound in response to MIDI commands, or
extracted for use by an application. (The terminology reflects musicians'
use of the word "sample" to refer collectively to a series of contiguous
audio samples or frames, rather than to a single, instantaneous sample.)
The data class for an audio sample will be an object that encapsulates
the audio sample data itself and information about how to interpret it
(the format of the audio data), such as an

AudioInputStream

.

Embedded sequences. A sound bank may contain built-in song data stored
in a data object such as a

Sequence

.

Synthesizers that use wavetable synthesis or related techniques play back the
audio in a sample when synthesizing notes, often when emulating the
real-world instrument that was originally recorded. However, there is not
necessarily a one-to-one correspondence between the

Instruments

and
samples in a

Soundbank

. A single

Instrument

can use multiple
SoundbankResources (typically for notes of dissimilar pitch or brightness).
Also, more than one

Instrument

can use the same sample.

public abstract class

SoundbankResource

extends

Object

A

SoundbankResource

represents any audio resource stored in a

Soundbank

. Common soundbank resources include:

- Instruments. An instrument may be specified in a variety of ways.
However, all soundbanks have some mechanism for defining instruments. In
doing so, they may reference other resources stored in the soundbank.
Each instrument has a

Patch

which specifies the MIDI program and
bank by which it may be referenced in MIDI messages. Instrument information
may be stored in

Instrument

objects.

Audio samples. A sample typically is a sampled audio waveform which
contains a short sound recording whose duration is a fraction of a
second, or at most a few seconds. These audio samples may be used by a

Synthesizer

to synthesize sound in response to MIDI commands, or
extracted for use by an application. (The terminology reflects musicians'
use of the word "sample" to refer collectively to a series of contiguous
audio samples or frames, rather than to a single, instantaneous sample.)
The data class for an audio sample will be an object that encapsulates
the audio sample data itself and information about how to interpret it
(the format of the audio data), such as an

AudioInputStream

.

Embedded sequences. A sound bank may contain built-in song data stored
in a data object such as a

Sequence

.

Synthesizers that use wavetable synthesis or related techniques play back the
audio in a sample when synthesizing notes, often when emulating the
real-world instrument that was originally recorded. However, there is not
necessarily a one-to-one correspondence between the

Instruments

and
samples in a

Soundbank

. A single

Instrument

can use multiple
SoundbankResources (typically for notes of dissimilar pitch or brightness).
Also, more than one

Instrument

can use the same sample.

Instruments. An instrument may be specified in a variety of ways.
However, all soundbanks have some mechanism for defining instruments. In
doing so, they may reference other resources stored in the soundbank.
Each instrument has a

Patch

which specifies the MIDI program and
bank by which it may be referenced in MIDI messages. Instrument information
may be stored in

Instrument

objects.

Audio samples. A sample typically is a sampled audio waveform which
contains a short sound recording whose duration is a fraction of a
second, or at most a few seconds. These audio samples may be used by a

Synthesizer

to synthesize sound in response to MIDI commands, or
extracted for use by an application. (The terminology reflects musicians'
use of the word "sample" to refer collectively to a series of contiguous
audio samples or frames, rather than to a single, instantaneous sample.)
The data class for an audio sample will be an object that encapsulates
the audio sample data itself and information about how to interpret it
(the format of the audio data), such as an

AudioInputStream

.

Embedded sequences. A sound bank may contain built-in song data stored
in a data object such as a

Sequence

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SoundbankResource

​(

Soundbank

soundBank,

String

name,

Class

<?> dataClass)

Constructs a new

SoundbankResource

from the given sound bank and
wavetable index.

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

Object

getData

()

Obtains the sampled audio that is stored in this

SoundbankResource

.

Class

<?>

getDataClass

()

Obtains the class used by this sample to represent its data.

String

getName

()

Obtains the name of the resource.

Soundbank

getSoundbank

()

Obtains the sound bank that contains this

SoundbankResource

.

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

Modifier

Constructor

Description

protected

SoundbankResource

​(

Soundbank

soundBank,

String

name,

Class

<?> dataClass)

Constructs a new

SoundbankResource

from the given sound bank and
wavetable index.

---

#### Constructor Summary

Constructs a new

SoundbankResource

from the given sound bank and
wavetable index.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Object

getData

()

Obtains the sampled audio that is stored in this

SoundbankResource

.

Class

<?>

getDataClass

()

Obtains the class used by this sample to represent its data.

String

getName

()

Obtains the name of the resource.

Soundbank

getSoundbank

()

Obtains the sound bank that contains this

SoundbankResource

.

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

Obtains the sampled audio that is stored in this

SoundbankResource

.

Obtains the class used by this sample to represent its data.

Obtains the name of the resource.

Obtains the sound bank that contains this

SoundbankResource

.

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

- SoundbankResource

```java
protected SoundbankResource​(
Soundbank
soundBank,

String
name,

Class
<?> dataClass)
```

Constructs a new

SoundbankResource

from the given sound bank and
wavetable index. (Setting the

SoundbankResource's

name, sampled
audio data, and instruments is a subclass responsibility.)

**Parameters:** soundBank

- the sound bank containing this

SoundbankResource
**Parameters:** name

- the name of the sample
**Parameters:** dataClass

- the class used to represent the sample's data
**See Also:** getSoundbank()

,

getName()

,

getDataClass()

,

getData()

============ METHOD DETAIL ==========

- Method Detail

- getSoundbank

```java
public
Soundbank
getSoundbank()
```

Obtains the sound bank that contains this

SoundbankResource

.

**Returns:** the sound bank in which this

SoundbankResource

is stored

- getName

```java
public
String
getName()
```

Obtains the name of the resource. This should generally be a string
descriptive of the resource.

**Returns:** the instrument's name

- getDataClass

```java
public
Class
<?> getDataClass()
```

Obtains the class used by this sample to represent its data. The object
returned by

getData

will be of this class. If this

SoundbankResource

object does not support direct access to its
data, returns

null

.

**Returns:** the class used to represent the sample's data, or null if the
data is not accessible

- getData

```java
public abstract
Object
getData()
```

Obtains the sampled audio that is stored in this

SoundbankResource

. The type of object returned depends on the
implementation of the concrete class, and may be queried using

getDataClass

.

**Returns:** an object containing the sampled audio data
**See Also:** getDataClass()

Constructor Detail

- SoundbankResource

```java
protected SoundbankResource​(
Soundbank
soundBank,

String
name,

Class
<?> dataClass)
```

Constructs a new

SoundbankResource

from the given sound bank and
wavetable index. (Setting the

SoundbankResource's

name, sampled
audio data, and instruments is a subclass responsibility.)

**Parameters:** soundBank

- the sound bank containing this

SoundbankResource
**Parameters:** name

- the name of the sample
**Parameters:** dataClass

- the class used to represent the sample's data
**See Also:** getSoundbank()

,

getName()

,

getDataClass()

,

getData()

---

#### Constructor Detail

SoundbankResource

```java
protected SoundbankResource​(
Soundbank
soundBank,

String
name,

Class
<?> dataClass)
```

Constructs a new

SoundbankResource

from the given sound bank and
wavetable index. (Setting the

SoundbankResource's

name, sampled
audio data, and instruments is a subclass responsibility.)

**Parameters:** soundBank

- the sound bank containing this

SoundbankResource
**Parameters:** name

- the name of the sample
**Parameters:** dataClass

- the class used to represent the sample's data
**See Also:** getSoundbank()

,

getName()

,

getDataClass()

,

getData()

---

#### SoundbankResource

protected SoundbankResource​(

Soundbank

soundBank,

String

name,

Class

<?> dataClass)

Constructs a new

SoundbankResource

from the given sound bank and
wavetable index. (Setting the

SoundbankResource's

name, sampled
audio data, and instruments is a subclass responsibility.)

Method Detail

- getSoundbank

```java
public
Soundbank
getSoundbank()
```

Obtains the sound bank that contains this

SoundbankResource

.

**Returns:** the sound bank in which this

SoundbankResource

is stored

- getName

```java
public
String
getName()
```

Obtains the name of the resource. This should generally be a string
descriptive of the resource.

**Returns:** the instrument's name

- getDataClass

```java
public
Class
<?> getDataClass()
```

Obtains the class used by this sample to represent its data. The object
returned by

getData

will be of this class. If this

SoundbankResource

object does not support direct access to its
data, returns

null

.

**Returns:** the class used to represent the sample's data, or null if the
data is not accessible

- getData

```java
public abstract
Object
getData()
```

Obtains the sampled audio that is stored in this

SoundbankResource

. The type of object returned depends on the
implementation of the concrete class, and may be queried using

getDataClass

.

**Returns:** an object containing the sampled audio data
**See Also:** getDataClass()

---

#### Method Detail

getSoundbank

```java
public
Soundbank
getSoundbank()
```

Obtains the sound bank that contains this

SoundbankResource

.

**Returns:** the sound bank in which this

SoundbankResource

is stored

---

#### getSoundbank

public

Soundbank

getSoundbank()

Obtains the sound bank that contains this

SoundbankResource

.

getName

```java
public
String
getName()
```

Obtains the name of the resource. This should generally be a string
descriptive of the resource.

**Returns:** the instrument's name

---

#### getName

public

String

getName()

Obtains the name of the resource. This should generally be a string
descriptive of the resource.

getDataClass

```java
public
Class
<?> getDataClass()
```

Obtains the class used by this sample to represent its data. The object
returned by

getData

will be of this class. If this

SoundbankResource

object does not support direct access to its
data, returns

null

.

**Returns:** the class used to represent the sample's data, or null if the
data is not accessible

---

#### getDataClass

public

Class

<?> getDataClass()

Obtains the class used by this sample to represent its data. The object
returned by

getData

will be of this class. If this

SoundbankResource

object does not support direct access to its
data, returns

null

.

getData

```java
public abstract
Object
getData()
```

Obtains the sampled audio that is stored in this

SoundbankResource

. The type of object returned depends on the
implementation of the concrete class, and may be queried using

getDataClass

.

**Returns:** an object containing the sampled audio data
**See Also:** getDataClass()

---

#### getData

public abstract

Object

getData()

Obtains the sampled audio that is stored in this

SoundbankResource

. The type of object returned depends on the
implementation of the concrete class, and may be queried using

getDataClass

.

---

