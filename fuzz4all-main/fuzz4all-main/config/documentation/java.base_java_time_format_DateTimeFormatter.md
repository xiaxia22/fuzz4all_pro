# Class DateTimeFormatter

**Source:** `java.base\java\time\format\DateTimeFormatter.html`

### Class Description

```java
public final class
DateTimeFormatter

extends
Object
```

Formatter for printing and parsing date-time objects.

This class provides the main application entry point for printing and parsing
and provides common implementations of

DateTimeFormatter

:

- Using predefined constants, such as

ISO_LOCAL_DATE
- Using pattern letters, such as

uuuu-MMM-dd
- Using localized styles, such as

long

or

medium

More complex formatters are provided by

DateTimeFormatterBuilder

.

The main date-time classes provide two methods - one for formatting,

format(DateTimeFormatter formatter)

, and one for parsing,

parse(CharSequence text, DateTimeFormatter formatter)

.

For example:

```java
LocalDate date = LocalDate.now();
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

In addition to the format, formatters can be created with desired Locale,
Chronology, ZoneId, and DecimalStyle.

The

withLocale

method returns a new formatter that
overrides the locale. The locale affects some aspects of formatting and
parsing. For example, the

ofLocalizedDate

provides a
formatter that uses the locale specific date format.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8

---

### Field Details

#### public static final
DateTimeFormatter
ISO_LOCAL_DATE

The ISO date formatter that formats or parses a date without an
offset, such as '2011-12-03'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

A dash

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_OFFSET_DATE

The ISO date formatter that formats or parses a date with an
offset, such as '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date format.
The format consists of:

- The

ISO_LOCAL_DATE

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_DATE

The ISO date formatter that formats or parses a date with the
offset if available, such as '2011-12-03' or '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended date format.
The format consists of:

- The

ISO_LOCAL_DATE

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_LOCAL_TIME

The ISO time formatter that formats or parses a time without an
offset, such as '10:15' or '10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local time format.
The format consists of:

- Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then the format is complete.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

If the nano-of-second is zero or not available then the format is complete.

A decimal point

One to nine digits for the

nano-of-second

.
As many digits will be output as required.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_OFFSET_TIME

The ISO time formatter that formats or parses a time with an
offset, such as '10:15+01:00' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_TIME

The ISO time formatter that formats or parses a time, with the
offset if available, such as '10:15', '10:15:30' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_LOCAL_DATE_TIME

The ISO date-time formatter that formats or parses a date-time without
an offset, such as '2011-12-03T10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE

The letter 'T'. Parsing is case insensitive.

The

ISO_LOCAL_TIME

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_OFFSET_DATE_TIME

The ISO date-time formatter that formats or parses a date-time with an
offset, such as '2011-12-03T10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_ZONED_DATE_TIME

The ISO-like date-time formatter that formats or parses a date-time with
offset and zone, such as '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
a format that extends the ISO-8601 extended offset date-time format
to add the time-zone.
The section in square brackets is not part of the ISO-8601 standard.
The format consists of:

- The

ISO_OFFSET_DATE_TIME

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_DATE_TIME

The ISO-like date-time formatter that formats or parses a date-time with
the offset and zone if available, such as '2011-12-03T10:15:30',
'2011-12-03T10:15:30+01:00' or '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local or offset date-time format, as well as the
extended non-ISO form specifying the time-zone.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_ORDINAL_DATE

The ISO date formatter that formats or parses the ordinal date
without an offset, such as '2012-337'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended ordinal date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Three digits for the

day-of-year

.
This is pre-padded by zero to ensure three digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_WEEK_DATE

The ISO date formatter that formats or parses the week-based date
without an offset, such as '2012-W48-6'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended week-based date format.
The format consists of:

- Four digits or more for the

week-based-year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

The letter 'W'. Parsing is case insensitive.

Two digits for the

week-of-week-based-year

.
This is pre-padded by zero to ensure three digits.

A dash

One digit for the

day-of-week

.
The value run from Monday (1) to Sunday (7).

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
ISO_INSTANT

The ISO instant formatter that formats or parses an instant in UTC,
such as '2011-12-03T10:15:30Z'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 instant format.
When formatting, the second-of-minute is always output.
The nano-of-second outputs zero, three, six or nine digits as necessary.
When parsing, time to at least the seconds field is required.
Fractional seconds from zero to nine are parsed.
The localized decimal style is not used.

This is a special case formatter intended to allow a human readable form
of an

Instant

. The

Instant

class is designed to
only represent a point in time and internally stores a value in nanoseconds
from a fixed epoch of 1970-01-01Z. As such, an

Instant

cannot be
formatted as a date or time without providing some form of time-zone.
This formatter allows the

Instant

to be formatted, by providing
a suitable conversion using

ZoneOffset.UTC

.

The format consists of:

- The

ISO_OFFSET_DATE_TIME

where the instant is converted from

ChronoField.INSTANT_SECONDS

and

ChronoField.NANO_OF_SECOND

using the

UTC

offset. Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
BASIC_ISO_DATE

The ISO date formatter that formats or parses a date without an
offset, such as '20111203'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 basic local date format.
The format consists of:

- Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

without colons. If the offset has
seconds then they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### public static final
DateTimeFormatter
RFC_1123_DATE_TIME

The RFC-1123 date-time formatter, such as 'Tue, 3 Jun 2008 11:05:30 GMT'.

This returns an immutable formatter capable of formatting and parsing
most of the RFC-1123 format.
RFC-1123 updates RFC-822 changing the year from two digits to four.
This implementation requires a four digit year.
This implementation also does not handle North American or military zone
names, only 'GMT' and offset amounts.

The format consists of:

- If the day-of-week is not available to format or parse then jump to day-of-month.

Three letter

day-of-week

in English.

A comma

A space

One or two digits for the

day-of-month

.

A space

Three letter

month-of-year

in English.

A space

Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

A space

Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then jump to the next space.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

A space

The

offset ID

without colons or seconds.
An offset of zero uses "GMT". North American zone names and military zone names are not handled.

Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
DateTimeFormatter
ofPattern​(
String
pattern)

Creates a formatter using the specified pattern.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the

default FORMAT locale

.
This can be changed using

withLocale(Locale)

on the returned formatter.
Alternatively use the

ofPattern(String, Locale)

variant of this method.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

**Parameters:**
- pattern

- the pattern to use, not null

**Returns:**
- the formatter based on the pattern, not null

**Throws:**
- IllegalArgumentException

- if the pattern is invalid

**See Also:**
- DateTimeFormatterBuilder.appendPattern(String)

---

#### public static
DateTimeFormatter
ofPattern​(
String
pattern,

Locale
locale)

Creates a formatter using the specified pattern and locale.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the specified locale.
This can be changed using

withLocale(Locale)

on the returned formatter.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

**Parameters:**
- pattern

- the pattern to use, not null
- locale

- the locale to use, not null

**Returns:**
- the formatter based on the pattern, not null

**Throws:**
- IllegalArgumentException

- if the pattern is invalid

**See Also:**
- DateTimeFormatterBuilder.appendPattern(String)

---

#### public static
DateTimeFormatter
ofLocalizedDate​(
FormatStyle
dateStyle)

Returns a locale specific date format for the ISO chronology.

This returns a formatter that will format or parse a date.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

**Parameters:**
- dateStyle

- the formatter style to obtain, not null

**Returns:**
- the date formatter, not null

---

#### public static
DateTimeFormatter
ofLocalizedTime​(
FormatStyle
timeStyle)

Returns a locale specific time format for the ISO chronology.

This returns a formatter that will format or parse a time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:**
- timeStyle

- the formatter style to obtain, not null

**Returns:**
- the time formatter, not null

---

#### public static
DateTimeFormatter
ofLocalizedDateTime​(
FormatStyle
dateTimeStyle)

Returns a locale specific date-time formatter for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:**
- dateTimeStyle

- the formatter style to obtain, not null

**Returns:**
- the date-time formatter, not null

---

#### public static
DateTimeFormatter
ofLocalizedDateTime​(
FormatStyle
dateStyle,

FormatStyle
timeStyle)

Returns a locale specific date and time format for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:**
- dateStyle

- the date formatter style to obtain, not null
- timeStyle

- the time formatter style to obtain, not null

**Returns:**
- the date, time or date-time formatter, not null

---

#### public static final
TemporalQuery
<
Period
> parsedExcessDays()

A query that provides access to the excess days that were parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null period, with a zero period returned instead of null.

There are two situations where this query may return a non-zero period.

- If the

ResolverStyle

is

LENIENT

and a time is parsed
without a date, then the complete result of the parse consists of a

LocalTime

and an excess

Period

in days.

If the

ResolverStyle

is

SMART

and a time is parsed
without a date where the time is 24:00:00, then the complete result of
the parse consists of a

LocalTime

of 00:00:00 and an excess

Period

of one day.

In both cases, if a complete

ChronoLocalDateTime

or

Instant

is parsed, then the excess days are added to the date part.
As a result, this query will return a zero period.

The

SMART

behaviour handles the common "end of day" 24:00 value.
Processing in

LENIENT

mode also produces the same result:

```java
Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)
```

The query can be used as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());
```

**Returns:**
- a query that provides access to the excess days that were parsed

---

#### public static final
TemporalQuery
<
Boolean
> parsedLeapSecond()

A query that provides access to whether a leap-second was parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null boolean, true if parsing saw a leap-second, false if not.

Instant parsing handles the special "leap second" time of '23:59:60'.
Leap seconds occur at '23:59:60' in the UTC time-zone, but at other
local times in different time-zones. To avoid this potential ambiguity,
the handling of leap-seconds is limited to

DateTimeFormatterBuilder.appendInstant()

, as that method
always parses the instant with the UTC zone offset.

If the time '23:59:60' is received, then a simple conversion is applied,
replacing the second-of-minute of 60 with 59. This query can be used
on the parse result to determine if the leap-second adjustment was made.
The query will return

true

if it did adjust to remove the
leap-second, and

false

if not. Note that applying a leap-second
smoothing mechanism, such as UTC-SLS, is the responsibility of the
application, as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
Instant instant = parsed.query(Instant::from);
if (parsed.query(DateTimeFormatter.parsedLeapSecond())) {
// validate leap-second is correct and apply correct smoothing
}
```

**Returns:**
- a query that provides access to whether a leap-second was parsed

---

#### public
Locale
getLocale()

Gets the locale to be used during formatting.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

**Returns:**
- the locale of this formatter, not null

---

#### public
DateTimeFormatter
withLocale​(
Locale
locale)

Returns a copy of this formatter with a new locale.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

The locale is stored as passed in, without further processing.
If the locale has

Unicode extensions

, they may be used later in text
processing. To set the chronology, time-zone and decimal style from
unicode extensions, see

localizedBy()

.

This instance is immutable and unaffected by this method call.

**Parameters:**
- locale

- the new locale, not null

**Returns:**
- a formatter based on this formatter with the requested locale, not null

**See Also:**
- localizedBy(Locale)

---

#### public
DateTimeFormatter
localizedBy​(
Locale
locale)

Returns a copy of this formatter with localized values of the locale,
calendar, region, decimal style and/or timezone, that supercede values in
this formatter.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern. If the locale contains the
"ca" (calendar), "nu" (numbering system), "rg" (region override), and/or
"tz" (timezone)

Unicode extensions

,
the chronology, numbering system and/or the zone are overridden. If both "ca"
and "rg" are specified, the chronology from the "ca" extension supersedes the
implicit one from the "rg" extension. Same is true for the "nu" extension.

Unlike the

withLocale

method, the call to this method may
produce a different formatter depending on the order of method chaining with
other withXXXX() methods.

This instance is immutable and unaffected by this method call.

**Parameters:**
- locale

- the locale, not null

**Returns:**
- a formatter based on this formatter with localized values of
the calendar, decimal style and/or timezone, that supercede values in this
formatter.

**See Also:**
- withLocale(Locale)

**Since:**
- 10

---

#### public
DecimalStyle
getDecimalStyle()

Gets the DecimalStyle to be used during formatting.

**Returns:**
- the locale of this formatter, not null

---

#### public
DateTimeFormatter
withDecimalStyle​(
DecimalStyle
decimalStyle)

Returns a copy of this formatter with a new DecimalStyle.

This instance is immutable and unaffected by this method call.

**Parameters:**
- decimalStyle

- the new DecimalStyle, not null

**Returns:**
- a formatter based on this formatter with the requested DecimalStyle, not null

---

#### public
Chronology
getChronology()

Gets the overriding chronology to be used during formatting.

This returns the override chronology, used to convert dates.
By default, a formatter has no override chronology, returning null.
See

withChronology(Chronology)

for more details on overriding.

**Returns:**
- the override chronology of this formatter, null if no override

---

#### public
DateTimeFormatter
withChronology​(
Chronology
chrono)

Returns a copy of this formatter with a new override chronology.

This returns a formatter with similar state to this formatter but
with the override chronology set.
By default, a formatter has no override chronology, returning null.

If an override is added, then any date that is formatted or parsed will be affected.

When formatting, if the temporal object contains a date, then it will
be converted to a date in the override chronology.
Whether the temporal contains a date is determined by querying the

EPOCH_DAY

field.
Any time or zone will be retained unaltered unless overridden.

If the temporal object does not contain a date, but does contain one
or more

ChronoField

date fields, then a

DateTimeException

is thrown. In all other cases, the override chronology is added to the temporal,
replacing any previous chronology, but without changing the date/time.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

**Parameters:**
- chrono

- the new chronology, null if no override

**Returns:**
- a formatter based on this formatter with the requested override chronology, not null

---

#### public
ZoneId
getZone()

Gets the overriding zone to be used during formatting.

This returns the override zone, used to convert instants.
By default, a formatter has no override zone, returning null.
See

withZone(ZoneId)

for more details on overriding.

**Returns:**
- the override zone of this formatter, null if no override

---

#### public
DateTimeFormatter
withZone​(
ZoneId
zone)

Returns a copy of this formatter with a new override zone.

This returns a formatter with similar state to this formatter but
with the override zone set.
By default, a formatter has no override zone, returning null.

If an override is added, then any instant that is formatted or parsed will be affected.

When formatting, if the temporal object contains an instant, then it will
be converted to a zoned date-time using the override zone.
Whether the temporal is an instant is determined by querying the

INSTANT_SECONDS

field.
If the input has a chronology then it will be retained unless overridden.
If the input does not have a chronology, such as

Instant

, then
the ISO chronology will be used.

If the temporal object does not contain an instant, but does contain
an offset then an additional check is made. If the normalized override
zone is an offset that differs from the offset of the temporal, then
a

DateTimeException

is thrown. In all other cases, the override
zone is added to the temporal, replacing any previous zone, but without
changing the date/time.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

**Parameters:**
- zone

- the new override zone, null if no override

**Returns:**
- a formatter based on this formatter with the requested override zone, not null

---

#### public
ResolverStyle
getResolverStyle()

Gets the resolver style to use during parsing.

This returns the resolver style, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has the

SMART

resolver style.
See

withResolverStyle(ResolverStyle)

for more details.

**Returns:**
- the resolver style of this formatter, not null

---

#### public
DateTimeFormatter
withResolverStyle​(
ResolverStyle
resolverStyle)

Returns a copy of this formatter with a new resolver style.

This returns a formatter with similar state to this formatter but
with the resolver style set. By default, a formatter has the

SMART

resolver style.

Changing the resolver style only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver style is used to control how phase 2, resolving, happens.
See

ResolverStyle

for more information on the options available.

This instance is immutable and unaffected by this method call.

**Parameters:**
- resolverStyle

- the new resolver style, not null

**Returns:**
- a formatter based on this formatter with the requested resolver style, not null

---

#### public
Set
<
TemporalField
> getResolverFields()

Gets the resolver fields to use during parsing.

This returns the resolver fields, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has no resolver fields, and thus returns null.
See

withResolverFields(Set)

for more details.

**Returns:**
- the immutable set of resolver fields of this formatter, null if no fields

---

#### public
DateTimeFormatter
withResolverFields​(
TemporalField
... resolverFields)

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

**Parameters:**
- resolverFields

- the new set of resolver fields, null if no fields

**Returns:**
- a formatter based on this formatter with the requested resolver style, not null

---

#### public
DateTimeFormatter
withResolverFields​(
Set
<
TemporalField
> resolverFields)

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

**Parameters:**
- resolverFields

- the new set of resolver fields, null if no fields

**Returns:**
- a formatter based on this formatter with the requested resolver style, not null

---

#### public
String
format​(
TemporalAccessor
temporal)

Formats a date-time object using this formatter.

This formats the date-time to a String using the rules of the formatter.

**Parameters:**
- temporal

- the temporal object to format, not null

**Returns:**
- the formatted string, not null

**Throws:**
- DateTimeException

- if an error occurs during formatting

---

#### public void formatTo​(
TemporalAccessor
temporal,

Appendable
appendable)

Formats a date-time object to an

Appendable

using this formatter.

This outputs the formatted date-time to the specified destination.

Appendable

is a general purpose interface that is implemented by all
key character output classes including

StringBuffer

,

StringBuilder

,

PrintStream

and

Writer

.

Although

Appendable

methods throw an

IOException

, this method does not.
Instead, any

IOException

is wrapped in a runtime exception.

**Parameters:**
- temporal

- the temporal object to format, not null
- appendable

- the appendable to format to, not null

**Throws:**
- DateTimeException

- if an error occurs during formatting

---

#### public
TemporalAccessor
parse​(
CharSequence
text)

Fully parses the text producing a temporal object.

This parses the entire text producing a temporal object.
It is typically more useful to use

parse(CharSequence, TemporalQuery)

.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Parameters:**
- text

- the text to parse, not null

**Returns:**
- the parsed temporal object, not null

**Throws:**
- DateTimeParseException

- if unable to parse the requested result

---

#### public
TemporalAccessor
parse​(
CharSequence
text,

ParsePosition
position)

Parses the text using this formatter, providing control over the text position.

This parses the text without requiring the parse to start from the beginning
of the string or finish at the end.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

The operation of this method is slightly different to similar methods using

ParsePosition

on

java.text.Format

. That class will return
errors using the error index on the

ParsePosition

. By contrast, this
method will throw a

DateTimeParseException

if an error occurs, with
the exception containing the error index.
This change in behavior is necessary due to the increased complexity of
parsing and resolving dates/times in this API.

If the formatter parses the same field more than once with different values,
the result will be an error.

**Parameters:**
- text

- the text to parse, not null
- position

- the position to parse from, updated with length parsed
and the index of any error, not null

**Returns:**
- the parsed temporal object, not null

**Throws:**
- DateTimeParseException

- if unable to parse the requested result
- IndexOutOfBoundsException

- if the position is invalid

---

#### public <T> T parse​(
CharSequence
text,

TemporalQuery
<T> query)

Fully parses the text producing an object of the specified type.

Most applications should use this method for parsing.
It parses the entire text to produce the required date-time.
The query is typically a method reference to a

from(TemporalAccessor)

method.
For example:

```java
LocalDateTime dt = parser.parse(str, LocalDateTime::from);
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Parameters:**
- text

- the text to parse, not null
- query

- the query defining the type to parse to, not null

**Returns:**
- the parsed date-time, not null

**Throws:**
- DateTimeParseException

- if unable to parse the requested result

**Type Parameters:**
- T

- the type of the parsed date-time

---

#### public
TemporalAccessor
parseBest​(
CharSequence
text,

TemporalQuery
<?>... queries)

Fully parses the text producing an object of one of the specified types.

This parse method is convenient for use when the parser can handle optional elements.
For example, a pattern of 'uuuu-MM-dd HH.mm[ VV]' can be fully parsed to a

ZonedDateTime

,
or partially parsed to a

LocalDateTime

.
The queries must be specified in order, starting from the best matching full-parse option
and ending with the worst matching minimal parse option.
The query is typically a method reference to a

from(TemporalAccessor)

method.

The result is associated with the first type that successfully parses.
Normally, applications will use

instanceof

to check the result.
For example:

```java
TemporalAccessor dt = parser.parseBest(str, ZonedDateTime::from, LocalDateTime::from);
if (dt instanceof ZonedDateTime) {
...
} else {
...
}
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Parameters:**
- text

- the text to parse, not null
- queries

- the queries defining the types to attempt to parse to,
must implement

TemporalAccessor

, not null

**Returns:**
- the parsed date-time, not null

**Throws:**
- IllegalArgumentException

- if less than 2 types are specified
- DateTimeParseException

- if unable to parse the requested result

---

#### public
TemporalAccessor
parseUnresolved​(
CharSequence
text,

ParsePosition
position)

Parses the text using this formatter, without resolving the result, intended
for advanced use cases.

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.
This method performs the parsing stage but not the resolving stage.

The result of this method is

TemporalAccessor

which represents the
data as seen in the input. Values are not validated, thus parsing a date string
of '2012-00-65' would result in a temporal with three fields - year of '2012',
month of '0' and day-of-month of '65'.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

Errors are returned using the error index field of the

ParsePosition

instead of

DateTimeParseException

.
The returned error index will be set to an index indicative of the error.
Callers must check for errors before using the result.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

**Parameters:**
- text

- the text to parse, not null
- position

- the position to parse from, updated with length parsed
and the index of any error, not null

**Returns:**
- the parsed text, null if the parse results in an error

**Throws:**
- DateTimeException

- if some problem occurs during parsing
- IndexOutOfBoundsException

- if the position is invalid

---

#### public
Format
toFormat()

Returns this formatter as a

java.text.Format

instance.

The returned

Format

instance will format any

TemporalAccessor

and parses to a resolved

TemporalAccessor

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

**Returns:**
- this formatter as a classic format instance, not null

---

#### public
Format
toFormat​(
TemporalQuery
<?> parseQuery)

Returns this formatter as a

java.text.Format

instance that will
parse using the specified query.

The returned

Format

instance will format any

TemporalAccessor

and parses to the type specified.
The type must be one that is supported by

parse(java.lang.CharSequence)

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

**Parameters:**
- parseQuery

- the query defining the type to parse to, not null

**Returns:**
- this formatter as a classic format instance, not null

---

#### public
String
toString()

Returns a description of the underlying formatters.

**Overrides:**
- toString

in class

Object

**Returns:**
- a description of this formatter, not null

---

### Additional Sections

#### Class DateTimeFormatter

java.lang.Object

- java.time.format.DateTimeFormatter

java.time.format.DateTimeFormatter

```java
public final class
DateTimeFormatter

extends
Object
```

Formatter for printing and parsing date-time objects.

This class provides the main application entry point for printing and parsing
and provides common implementations of

DateTimeFormatter

:

- Using predefined constants, such as

ISO_LOCAL_DATE
- Using pattern letters, such as

uuuu-MMM-dd
- Using localized styles, such as

long

or

medium

More complex formatters are provided by

DateTimeFormatterBuilder

.

The main date-time classes provide two methods - one for formatting,

format(DateTimeFormatter formatter)

, and one for parsing,

parse(CharSequence text, DateTimeFormatter formatter)

.

For example:

```java
LocalDate date = LocalDate.now();
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

In addition to the format, formatters can be created with desired Locale,
Chronology, ZoneId, and DecimalStyle.

The

withLocale

method returns a new formatter that
overrides the locale. The locale affects some aspects of formatting and
parsing. For example, the

ofLocalizedDate

provides a
formatter that uses the locale specific date format.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

**Implementation Requirements:** This class is immutable and thread-safe.
**Since:** 1.8

public final class

DateTimeFormatter

extends

Object

Formatter for printing and parsing date-time objects.

This class provides the main application entry point for printing and parsing
and provides common implementations of

DateTimeFormatter

:

- Using predefined constants, such as

ISO_LOCAL_DATE
- Using pattern letters, such as

uuuu-MMM-dd
- Using localized styles, such as

long

or

medium

More complex formatters are provided by

DateTimeFormatterBuilder

.

The main date-time classes provide two methods - one for formatting,

format(DateTimeFormatter formatter)

, and one for parsing,

parse(CharSequence text, DateTimeFormatter formatter)

.

For example:

```java
LocalDate date = LocalDate.now();
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

In addition to the format, formatters can be created with desired Locale,
Chronology, ZoneId, and DecimalStyle.

The

withLocale

method returns a new formatter that
overrides the locale. The locale affects some aspects of formatting and
parsing. For example, the

ofLocalizedDate

provides a
formatter that uses the locale specific date format.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

This class provides the main application entry point for printing and parsing
and provides common implementations of

DateTimeFormatter

:

- Using predefined constants, such as

ISO_LOCAL_DATE
- Using pattern letters, such as

uuuu-MMM-dd
- Using localized styles, such as

long

or

medium

More complex formatters are provided by

DateTimeFormatterBuilder

.

The main date-time classes provide two methods - one for formatting,

format(DateTimeFormatter formatter)

, and one for parsing,

parse(CharSequence text, DateTimeFormatter formatter)

.

For example:

```java
LocalDate date = LocalDate.now();
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

In addition to the format, formatters can be created with desired Locale,
Chronology, ZoneId, and DecimalStyle.

The

withLocale

method returns a new formatter that
overrides the locale. The locale affects some aspects of formatting and
parsing. For example, the

ofLocalizedDate

provides a
formatter that uses the locale specific date format.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Using predefined constants, such as

ISO_LOCAL_DATE

Using pattern letters, such as

uuuu-MMM-dd

Using localized styles, such as

long

or

medium

More complex formatters are provided by

DateTimeFormatterBuilder

.

The main date-time classes provide two methods - one for formatting,

format(DateTimeFormatter formatter)

, and one for parsing,

parse(CharSequence text, DateTimeFormatter formatter)

.

For example:

```java
LocalDate date = LocalDate.now();
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

In addition to the format, formatters can be created with desired Locale,
Chronology, ZoneId, and DecimalStyle.

The

withLocale

method returns a new formatter that
overrides the locale. The locale affects some aspects of formatting and
parsing. For example, the

ofLocalizedDate

provides a
formatter that uses the locale specific date format.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The main date-time classes provide two methods - one for formatting,

format(DateTimeFormatter formatter)

, and one for parsing,

parse(CharSequence text, DateTimeFormatter formatter)

.

For example:

```java
LocalDate date = LocalDate.now();
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

In addition to the format, formatters can be created with desired Locale,
Chronology, ZoneId, and DecimalStyle.

The

withLocale

method returns a new formatter that
overrides the locale. The locale affects some aspects of formatting and
parsing. For example, the

ofLocalizedDate

provides a
formatter that uses the locale specific date format.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

For example:

```java
LocalDate date = LocalDate.now();
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

In addition to the format, formatters can be created with desired Locale,
Chronology, ZoneId, and DecimalStyle.

The

withLocale

method returns a new formatter that
overrides the locale. The locale affects some aspects of formatting and
parsing. For example, the

ofLocalizedDate

provides a
formatter that uses the locale specific date format.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

LocalDate date = LocalDate.now();
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);

In addition to the format, formatters can be created with desired Locale,
Chronology, ZoneId, and DecimalStyle.

The

withLocale

method returns a new formatter that
overrides the locale. The locale affects some aspects of formatting and
parsing. For example, the

ofLocalizedDate

provides a
formatter that uses the locale specific date format.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The

withLocale

method returns a new formatter that
overrides the locale. The locale affects some aspects of formatting and
parsing. For example, the

ofLocalizedDate

provides a
formatter that uses the locale specific date format.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The

withChronology

method returns a new formatter
that overrides the chronology. If overridden, the date-time value is
converted to the chronology before formatting. During parsing the date-time
value is converted to the chronology before it is returned.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The

withZone

method returns a new formatter that overrides
the zone. If overridden, the date-time value is converted to a ZonedDateTime
with the requested ZoneId before formatting. During parsing the ZoneId is
applied before the value is returned.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The

withDecimalStyle

method returns a new formatter that
overrides the

DecimalStyle

. The DecimalStyle symbols are used for
formatting and parsing.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Some applications may need to use the older

java.text.Format

class for formatting. The

toFormat()

method returns an
implementation of

java.text.Format

.

Predefined Formatters

Predefined Formatters

Formatter

Description

Example

ofLocalizedDate(dateStyle)

Formatter with date style from the locale

'2011-12-03'

ofLocalizedTime(timeStyle)

Formatter with time style from the locale

'10:15:30'

ofLocalizedDateTime(dateTimeStyle)

Formatter with a style for date and time from the locale

'3 Jun 2008 11:05:30'

ofLocalizedDateTime(dateStyle,timeStyle)

Formatter with date and time styles from the locale

'3 Jun 2008 11:05'

BASIC_ISO_DATE

Basic ISO date

'20111203'

ISO_LOCAL_DATE

ISO Local Date

'2011-12-03'

ISO_OFFSET_DATE

ISO Date with offset

'2011-12-03+01:00'

ISO_DATE

ISO Date with or without offset

'2011-12-03+01:00'; '2011-12-03'

ISO_LOCAL_TIME

Time without offset

'10:15:30'

ISO_OFFSET_TIME

Time with offset

'10:15:30+01:00'

ISO_TIME

Time with or without offset

'10:15:30+01:00'; '10:15:30'

ISO_LOCAL_DATE_TIME

ISO Local Date and Time

'2011-12-03T10:15:30'

ISO_OFFSET_DATE_TIME

Date Time with Offset

'2011-12-03T10:15:30+01:00'

ISO_ZONED_DATE_TIME

Zoned Date Time

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_DATE_TIME

Date and time with ZoneId

'2011-12-03T10:15:30+01:00[Europe/Paris]'

ISO_ORDINAL_DATE

Year and day of year

'2012-337'

ISO_WEEK_DATE

Year and Week

'2012-W48-6'

ISO_INSTANT

Date and Time of an Instant

'2011-12-03T10:15:30Z'

RFC_1123_DATE_TIME

RFC 1123 / RFC 822

'Tue, 3 Jun 2008 11:05:30 GMT'

Patterns for Formatting and Parsing

Patterns are based on a simple sequence of letters and symbols.
A pattern is used to create a Formatter using the

ofPattern(String)

and

ofPattern(String, Locale)

methods.
For example,

"d MMM uuuu"

will format 2011-12-03 as '3 Dec 2011'.
A formatter created from a pattern can be used as many times as necessary,
it is immutable and is thread-safe.

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

---

#### Patterns for Formatting and Parsing

For example:

```java
LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);
```

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

LocalDate date = LocalDate.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy MM dd");
String text = date.format(formatter);
LocalDate parsedDate = LocalDate.parse(text, formatter);

All letters 'A' to 'Z' and 'a' to 'z' are reserved as pattern letters. The
following pattern letters are defined:

Pattern Letters and Symbols

Symbol

Meaning

Presentation

Examples

G

era

text

AD; Anno Domini; A

u

year

year

2004; 04

y

year-of-era

year

2004; 04

D

day-of-year

number

189

M/L

month-of-year

number/text

7; 07; Jul; July; J

d

day-of-month

number

10

g

modified-julian-day

number

2451334

Q/q

quarter-of-year

number/text

3; 03; Q3; 3rd quarter

Y

week-based-year

year

1996; 96

w

week-of-week-based-year

number

27

W

week-of-month

number

4

E

day-of-week

text

Tue; Tuesday; T

e/c

localized day-of-week

number/text

2; 02; Tue; Tuesday; T

F

day-of-week-in-month

number

3

a

am-pm-of-day

text

PM

h

clock-hour-of-am-pm (1-12)

number

12

K

hour-of-am-pm (0-11)

number

0

k

clock-hour-of-day (1-24)

number

24

H

hour-of-day (0-23)

number

0

m

minute-of-hour

number

30

s

second-of-minute

number

55

S

fraction-of-second

fraction

978

A

milli-of-day

number

1234

n

nano-of-second

number

987654321

N

nano-of-day

number

1234000000

V

time-zone ID

zone-id

America/Los_Angeles; Z; -08:30

v

generic time-zone name

zone-name

Pacific Time; PT

z

time-zone name

zone-name

Pacific Standard Time; PST

O

localized zone-offset

offset-O

GMT+8; GMT+08:00; UTC-08:00

X

zone-offset 'Z' for zero

offset-X

Z; -08; -0830; -08:30; -083015; -08:30:15

x

zone-offset

offset-x

+0000; -08; -0830; -08:30; -083015; -08:30:15

Z

zone-offset

offset-Z

+0000; -0800; -08:00

p

pad next

pad modifier

1

'

escape for text

delimiter

''

single quote

literal

'

[

optional section start

]

optional section end

#

reserved for future use

{

reserved for future use

}

reserved for future use

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The count of pattern letters determines the format.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Text

: The text style is determined based on the number of pattern
letters used. Less than 4 pattern letters will use the

short form

. Exactly 4 pattern letters will use the

full form

. Exactly 5 pattern letters will use the

narrow form

.
Pattern letters 'L', 'c', and 'q' specify the stand-alone form of the text styles.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Number

: If the count of letters is one, then the value is output using
the minimum number of digits and without padding. Otherwise, the count of digits
is used as the width of the output field, with the value zero-padded as necessary.
The following pattern letters have constraints on the count of letters.
Only one letter of 'c' and 'F' can be specified.
Up to two letters of 'd', 'H', 'h', 'K', 'k', 'm', and 's' can be specified.
Up to three letters of 'D' can be specified.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Number/Text

: If the count of pattern letters is 3 or greater, use the
Text rules above. Otherwise use the Number rules above.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Fraction

: Outputs the nano-of-second field as a fraction-of-second.
The nano-of-second value has nine digits, thus the count of pattern letters
is from 1 to 9. If it is less than 9, then the nano-of-second value is
truncated, with only the most significant digits being output.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Year

: The count of letters determines the minimum field width below
which padding is used. If the count of letters is two, then a

reduced

two digit form is
used. For printing, this outputs the rightmost two digits. For parsing, this
will parse using the base value of 2000, resulting in a year within the range
2000 to 2099 inclusive. If the count of letters is less than four (but not
two), then the sign is only output for negative years as per

SignStyle.NORMAL

. Otherwise, the sign is output if the pad width is
exceeded, as per

SignStyle.EXCEEDS_PAD

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

ZoneId

: This outputs the time-zone ID, such as 'Europe/Paris'. If the
count of letters is two, then the time-zone ID is output. Any other count of
letters throws

IllegalArgumentException

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Zone names

: This outputs the display name of the time-zone ID. If the
pattern letter is 'z' the output is the daylight savings aware zone name.
If there is insufficient information to determine whether DST applies,
the name ignoring daylight savings time will be used.
If the count of letters is one, two or three, then the short name is output.
If the count of letters is four, then the full name is output.
Five or more letters throws

IllegalArgumentException

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

If the pattern letter is 'v' the output provides the zone name ignoring
daylight savings time. If the count of letters is one, then the short name is output.
If the count of letters is four, then the full name is output.
Two, three and five or more letters throw

IllegalArgumentException

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Offset X and x

: This formats the offset based on the number of pattern
letters. One letter outputs just the hour, such as '+01', unless the minute
is non-zero in which case the minute is also output, such as '+0130'. Two
letters outputs the hour and minute, without a colon, such as '+0130'. Three
letters outputs the hour and minute, with a colon, such as '+01:30'. Four
letters outputs the hour and minute and optional second, without a colon,
such as '+013015'. Five letters outputs the hour and minute and optional
second, with a colon, such as '+01:30:15'. Six or more letters throws

IllegalArgumentException

. Pattern letter 'X' (upper case) will output
'Z' when the offset to be output would be zero, whereas pattern letter 'x'
(lower case) will output '+00', '+0000', or '+00:00'.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Offset O

: This formats the localized offset based on the number of
pattern letters. One letter outputs the

short

form of the localized offset, which is localized offset text, such as 'GMT',
with hour without leading zero, optional 2-digit minute and second if
non-zero, and colon, for example 'GMT+8'. Four letters outputs the

full

form, which is localized offset text,
such as 'GMT, with 2-digit hour and minute field, optional second field
if non-zero, and colon, for example 'GMT+08:00'. Any other count of letters
throws

IllegalArgumentException

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Offset Z

: This formats the offset based on the number of pattern
letters. One, two or three letters outputs the hour and minute, without a
colon, such as '+0130'. The output will be '+0000' when the offset is zero.
Four letters outputs the

full

form of localized
offset, equivalent to four letters of Offset-O. The output will be the
corresponding localized offset text if the offset is zero. Five
letters outputs the hour, minute, with optional second if non-zero, with
colon. It outputs 'Z' if the offset is zero.
Six or more letters throws

IllegalArgumentException

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Optional section

: The optional section markers work exactly like
calling

DateTimeFormatterBuilder.optionalStart()

and

DateTimeFormatterBuilder.optionalEnd()

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Pad modifier

: Modifies the pattern that immediately follows to be
padded with spaces. The pad width is determined by the number of pattern
letters. This is the same as calling

DateTimeFormatterBuilder.padNext(int)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

For example, 'ppH' outputs the hour-of-day padded on the left with spaces to
a width of 2.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Any unrecognized letter is an error. Any non-letter character, other than
'[', ']', '{', '}', '#' and the single quote will be output directly.
Despite this, it is recommended to use single quotes around all characters
that you want to output directly to ensure that future changes do not break
your application.

Resolving

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

---

#### Resolving

Five parsing methods are supplied by this class.
Four of these perform both the parse and resolve phases.
The fifth method,

parseUnresolved(CharSequence, ParsePosition)

,
only performs the first phase, leaving the result unresolved.
As such, it is essentially a low-level operation.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The resolve phase is controlled by two parameters, set on this class.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The

ResolverStyle

is an enum that offers three different approaches,
strict, smart and lenient. The smart option is the default.
It can be set using

withResolverStyle(ResolverStyle)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The

withResolverFields(TemporalField...)

parameter allows the
set of fields that will be resolved to be filtered before resolving starts.
For example, if the formatter has parsed a year, month, day-of-month
and day-of-year, then there are two approaches to resolve a date:
(year + month + day-of-month) and (year + day-of-year).
The resolver fields allows one of the two approaches to be selected.
If no resolver fields are set then both approaches must result in the same date.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

Resolving separate fields to form a complete date and time is a complex
process with behaviour distributed across a number of classes.
It follows these steps:

- The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

The chronology is determined.
The chronology of the result is either the chronology that was parsed,
or if no chronology was parsed, it is the chronology set on this class,
or if that is null, it is

IsoChronology

.

The

ChronoField

date fields are resolved.
This is achieved using

Chronology.resolveDate(Map, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

Chronology

.

The

ChronoField

time fields are resolved.
This is documented on

ChronoField

and is the same for all chronologies.

Any fields that are not

ChronoField

are processed.
This is achieved using

TemporalField.resolve(Map, TemporalAccessor, ResolverStyle)

.
Documentation about field resolution is located in the implementation
of

TemporalField

.

The

ChronoField

date and time fields are re-resolved.
This allows fields in step four to produce

ChronoField

values
and have them be processed into dates and times.

A

LocalTime

is formed if there is at least an hour-of-day available.
This involves providing default values for minute, second and fraction of second.

Any remaining unresolved fields are cross-checked against any
date and/or time that was resolved. Thus, an earlier stage would resolve
(year + month + day-of-month) to a date, and this stage would check that
day-of-week was valid for the date.

If an

excess number of days

was parsed then it is added to the date if a date is available.

If a second-based field is present, but

LocalTime

was not parsed,
then the resolver ensures that milli, micro and nano second values are
available to meet the contract of

ChronoField

.
These will be set to zero if missing.

If both date and time were parsed and either an offset or zone is present,
the field

ChronoField.INSTANT_SECONDS

is created.
If an offset was parsed then the offset will be combined with the

LocalDateTime

to form the instant, with any zone ignored.
If a

ZoneId

was parsed without an offset then the zone will be
combined with the

LocalDateTime

to form the instant using the rules
of

ChronoLocalDateTime.atZone(ZoneId)

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

DateTimeFormatter

BASIC_ISO_DATE

The ISO date formatter that formats or parses a date without an
offset, such as '20111203'.

static

DateTimeFormatter

ISO_DATE

The ISO date formatter that formats or parses a date with the
offset if available, such as '2011-12-03' or '2011-12-03+01:00'.

static

DateTimeFormatter

ISO_DATE_TIME

The ISO-like date-time formatter that formats or parses a date-time with
the offset and zone if available, such as '2011-12-03T10:15:30',
'2011-12-03T10:15:30+01:00' or '2011-12-03T10:15:30+01:00[Europe/Paris]'.

static

DateTimeFormatter

ISO_INSTANT

The ISO instant formatter that formats or parses an instant in UTC,
such as '2011-12-03T10:15:30Z'.

static

DateTimeFormatter

ISO_LOCAL_DATE

The ISO date formatter that formats or parses a date without an
offset, such as '2011-12-03'.

static

DateTimeFormatter

ISO_LOCAL_DATE_TIME

The ISO date-time formatter that formats or parses a date-time without
an offset, such as '2011-12-03T10:15:30'.

static

DateTimeFormatter

ISO_LOCAL_TIME

The ISO time formatter that formats or parses a time without an
offset, such as '10:15' or '10:15:30'.

static

DateTimeFormatter

ISO_OFFSET_DATE

The ISO date formatter that formats or parses a date with an
offset, such as '2011-12-03+01:00'.

static

DateTimeFormatter

ISO_OFFSET_DATE_TIME

The ISO date-time formatter that formats or parses a date-time with an
offset, such as '2011-12-03T10:15:30+01:00'.

static

DateTimeFormatter

ISO_OFFSET_TIME

The ISO time formatter that formats or parses a time with an
offset, such as '10:15+01:00' or '10:15:30+01:00'.

static

DateTimeFormatter

ISO_ORDINAL_DATE

The ISO date formatter that formats or parses the ordinal date
without an offset, such as '2012-337'.

static

DateTimeFormatter

ISO_TIME

The ISO time formatter that formats or parses a time, with the
offset if available, such as '10:15', '10:15:30' or '10:15:30+01:00'.

static

DateTimeFormatter

ISO_WEEK_DATE

The ISO date formatter that formats or parses the week-based date
without an offset, such as '2012-W48-6'.

static

DateTimeFormatter

ISO_ZONED_DATE_TIME

The ISO-like date-time formatter that formats or parses a date-time with
offset and zone, such as '2011-12-03T10:15:30+01:00[Europe/Paris]'.

static

DateTimeFormatter

RFC_1123_DATE_TIME

The RFC-1123 date-time formatter, such as 'Tue, 3 Jun 2008 11:05:30 GMT'.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

format

​(

TemporalAccessor

temporal)

Formats a date-time object using this formatter.

void

formatTo

​(

TemporalAccessor

temporal,

Appendable

appendable)

Formats a date-time object to an

Appendable

using this formatter.

Chronology

getChronology

()

Gets the overriding chronology to be used during formatting.

DecimalStyle

getDecimalStyle

()

Gets the DecimalStyle to be used during formatting.

Locale

getLocale

()

Gets the locale to be used during formatting.

Set

<

TemporalField

>

getResolverFields

()

Gets the resolver fields to use during parsing.

ResolverStyle

getResolverStyle

()

Gets the resolver style to use during parsing.

ZoneId

getZone

()

Gets the overriding zone to be used during formatting.

DateTimeFormatter

localizedBy

​(

Locale

locale)

Returns a copy of this formatter with localized values of the locale,
calendar, region, decimal style and/or timezone, that supercede values in
this formatter.

static

DateTimeFormatter

ofLocalizedDate

​(

FormatStyle

dateStyle)

Returns a locale specific date format for the ISO chronology.

static

DateTimeFormatter

ofLocalizedDateTime

​(

FormatStyle

dateTimeStyle)

Returns a locale specific date-time formatter for the ISO chronology.

static

DateTimeFormatter

ofLocalizedDateTime

​(

FormatStyle

dateStyle,

FormatStyle

timeStyle)

Returns a locale specific date and time format for the ISO chronology.

static

DateTimeFormatter

ofLocalizedTime

​(

FormatStyle

timeStyle)

Returns a locale specific time format for the ISO chronology.

static

DateTimeFormatter

ofPattern

​(

String

pattern)

Creates a formatter using the specified pattern.

static

DateTimeFormatter

ofPattern

​(

String

pattern,

Locale

locale)

Creates a formatter using the specified pattern and locale.

TemporalAccessor

parse

​(

CharSequence

text)

Fully parses the text producing a temporal object.

TemporalAccessor

parse

​(

CharSequence

text,

ParsePosition

position)

Parses the text using this formatter, providing control over the text position.

<T> T

parse

​(

CharSequence

text,

TemporalQuery

<T> query)

Fully parses the text producing an object of the specified type.

TemporalAccessor

parseBest

​(

CharSequence

text,

TemporalQuery

<?>... queries)

Fully parses the text producing an object of one of the specified types.

static

TemporalQuery

<

Period

>

parsedExcessDays

()

A query that provides access to the excess days that were parsed.

static

TemporalQuery

<

Boolean

>

parsedLeapSecond

()

A query that provides access to whether a leap-second was parsed.

TemporalAccessor

parseUnresolved

​(

CharSequence

text,

ParsePosition

position)

Parses the text using this formatter, without resolving the result, intended
for advanced use cases.

Format

toFormat

()

Returns this formatter as a

java.text.Format

instance.

Format

toFormat

​(

TemporalQuery

<?> parseQuery)

Returns this formatter as a

java.text.Format

instance that will
parse using the specified query.

String

toString

()

Returns a description of the underlying formatters.

DateTimeFormatter

withChronology

​(

Chronology

chrono)

Returns a copy of this formatter with a new override chronology.

DateTimeFormatter

withDecimalStyle

​(

DecimalStyle

decimalStyle)

Returns a copy of this formatter with a new DecimalStyle.

DateTimeFormatter

withLocale

​(

Locale

locale)

Returns a copy of this formatter with a new locale.

DateTimeFormatter

withResolverFields

​(

TemporalField

... resolverFields)

Returns a copy of this formatter with a new set of resolver fields.

DateTimeFormatter

withResolverFields

​(

Set

<

TemporalField

> resolverFields)

Returns a copy of this formatter with a new set of resolver fields.

DateTimeFormatter

withResolverStyle

​(

ResolverStyle

resolverStyle)

Returns a copy of this formatter with a new resolver style.

DateTimeFormatter

withZone

​(

ZoneId

zone)

Returns a copy of this formatter with a new override zone.

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

DateTimeFormatter

BASIC_ISO_DATE

The ISO date formatter that formats or parses a date without an
offset, such as '20111203'.

static

DateTimeFormatter

ISO_DATE

The ISO date formatter that formats or parses a date with the
offset if available, such as '2011-12-03' or '2011-12-03+01:00'.

static

DateTimeFormatter

ISO_DATE_TIME

The ISO-like date-time formatter that formats or parses a date-time with
the offset and zone if available, such as '2011-12-03T10:15:30',
'2011-12-03T10:15:30+01:00' or '2011-12-03T10:15:30+01:00[Europe/Paris]'.

static

DateTimeFormatter

ISO_INSTANT

The ISO instant formatter that formats or parses an instant in UTC,
such as '2011-12-03T10:15:30Z'.

static

DateTimeFormatter

ISO_LOCAL_DATE

The ISO date formatter that formats or parses a date without an
offset, such as '2011-12-03'.

static

DateTimeFormatter

ISO_LOCAL_DATE_TIME

The ISO date-time formatter that formats or parses a date-time without
an offset, such as '2011-12-03T10:15:30'.

static

DateTimeFormatter

ISO_LOCAL_TIME

The ISO time formatter that formats or parses a time without an
offset, such as '10:15' or '10:15:30'.

static

DateTimeFormatter

ISO_OFFSET_DATE

The ISO date formatter that formats or parses a date with an
offset, such as '2011-12-03+01:00'.

static

DateTimeFormatter

ISO_OFFSET_DATE_TIME

The ISO date-time formatter that formats or parses a date-time with an
offset, such as '2011-12-03T10:15:30+01:00'.

static

DateTimeFormatter

ISO_OFFSET_TIME

The ISO time formatter that formats or parses a time with an
offset, such as '10:15+01:00' or '10:15:30+01:00'.

static

DateTimeFormatter

ISO_ORDINAL_DATE

The ISO date formatter that formats or parses the ordinal date
without an offset, such as '2012-337'.

static

DateTimeFormatter

ISO_TIME

The ISO time formatter that formats or parses a time, with the
offset if available, such as '10:15', '10:15:30' or '10:15:30+01:00'.

static

DateTimeFormatter

ISO_WEEK_DATE

The ISO date formatter that formats or parses the week-based date
without an offset, such as '2012-W48-6'.

static

DateTimeFormatter

ISO_ZONED_DATE_TIME

The ISO-like date-time formatter that formats or parses a date-time with
offset and zone, such as '2011-12-03T10:15:30+01:00[Europe/Paris]'.

static

DateTimeFormatter

RFC_1123_DATE_TIME

The RFC-1123 date-time formatter, such as 'Tue, 3 Jun 2008 11:05:30 GMT'.

---

#### Field Summary

The ISO date formatter that formats or parses a date without an
offset, such as '20111203'.

The ISO date formatter that formats or parses a date with the
offset if available, such as '2011-12-03' or '2011-12-03+01:00'.

The ISO-like date-time formatter that formats or parses a date-time with
the offset and zone if available, such as '2011-12-03T10:15:30',
'2011-12-03T10:15:30+01:00' or '2011-12-03T10:15:30+01:00[Europe/Paris]'.

The ISO instant formatter that formats or parses an instant in UTC,
such as '2011-12-03T10:15:30Z'.

The ISO date formatter that formats or parses a date without an
offset, such as '2011-12-03'.

The ISO date-time formatter that formats or parses a date-time without
an offset, such as '2011-12-03T10:15:30'.

The ISO time formatter that formats or parses a time without an
offset, such as '10:15' or '10:15:30'.

The ISO date formatter that formats or parses a date with an
offset, such as '2011-12-03+01:00'.

The ISO date-time formatter that formats or parses a date-time with an
offset, such as '2011-12-03T10:15:30+01:00'.

The ISO time formatter that formats or parses a time with an
offset, such as '10:15+01:00' or '10:15:30+01:00'.

The ISO date formatter that formats or parses the ordinal date
without an offset, such as '2012-337'.

The ISO time formatter that formats or parses a time, with the
offset if available, such as '10:15', '10:15:30' or '10:15:30+01:00'.

The ISO date formatter that formats or parses the week-based date
without an offset, such as '2012-W48-6'.

The ISO-like date-time formatter that formats or parses a date-time with
offset and zone, such as '2011-12-03T10:15:30+01:00[Europe/Paris]'.

The RFC-1123 date-time formatter, such as 'Tue, 3 Jun 2008 11:05:30 GMT'.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

format

​(

TemporalAccessor

temporal)

Formats a date-time object using this formatter.

void

formatTo

​(

TemporalAccessor

temporal,

Appendable

appendable)

Formats a date-time object to an

Appendable

using this formatter.

Chronology

getChronology

()

Gets the overriding chronology to be used during formatting.

DecimalStyle

getDecimalStyle

()

Gets the DecimalStyle to be used during formatting.

Locale

getLocale

()

Gets the locale to be used during formatting.

Set

<

TemporalField

>

getResolverFields

()

Gets the resolver fields to use during parsing.

ResolverStyle

getResolverStyle

()

Gets the resolver style to use during parsing.

ZoneId

getZone

()

Gets the overriding zone to be used during formatting.

DateTimeFormatter

localizedBy

​(

Locale

locale)

Returns a copy of this formatter with localized values of the locale,
calendar, region, decimal style and/or timezone, that supercede values in
this formatter.

static

DateTimeFormatter

ofLocalizedDate

​(

FormatStyle

dateStyle)

Returns a locale specific date format for the ISO chronology.

static

DateTimeFormatter

ofLocalizedDateTime

​(

FormatStyle

dateTimeStyle)

Returns a locale specific date-time formatter for the ISO chronology.

static

DateTimeFormatter

ofLocalizedDateTime

​(

FormatStyle

dateStyle,

FormatStyle

timeStyle)

Returns a locale specific date and time format for the ISO chronology.

static

DateTimeFormatter

ofLocalizedTime

​(

FormatStyle

timeStyle)

Returns a locale specific time format for the ISO chronology.

static

DateTimeFormatter

ofPattern

​(

String

pattern)

Creates a formatter using the specified pattern.

static

DateTimeFormatter

ofPattern

​(

String

pattern,

Locale

locale)

Creates a formatter using the specified pattern and locale.

TemporalAccessor

parse

​(

CharSequence

text)

Fully parses the text producing a temporal object.

TemporalAccessor

parse

​(

CharSequence

text,

ParsePosition

position)

Parses the text using this formatter, providing control over the text position.

<T> T

parse

​(

CharSequence

text,

TemporalQuery

<T> query)

Fully parses the text producing an object of the specified type.

TemporalAccessor

parseBest

​(

CharSequence

text,

TemporalQuery

<?>... queries)

Fully parses the text producing an object of one of the specified types.

static

TemporalQuery

<

Period

>

parsedExcessDays

()

A query that provides access to the excess days that were parsed.

static

TemporalQuery

<

Boolean

>

parsedLeapSecond

()

A query that provides access to whether a leap-second was parsed.

TemporalAccessor

parseUnresolved

​(

CharSequence

text,

ParsePosition

position)

Parses the text using this formatter, without resolving the result, intended
for advanced use cases.

Format

toFormat

()

Returns this formatter as a

java.text.Format

instance.

Format

toFormat

​(

TemporalQuery

<?> parseQuery)

Returns this formatter as a

java.text.Format

instance that will
parse using the specified query.

String

toString

()

Returns a description of the underlying formatters.

DateTimeFormatter

withChronology

​(

Chronology

chrono)

Returns a copy of this formatter with a new override chronology.

DateTimeFormatter

withDecimalStyle

​(

DecimalStyle

decimalStyle)

Returns a copy of this formatter with a new DecimalStyle.

DateTimeFormatter

withLocale

​(

Locale

locale)

Returns a copy of this formatter with a new locale.

DateTimeFormatter

withResolverFields

​(

TemporalField

... resolverFields)

Returns a copy of this formatter with a new set of resolver fields.

DateTimeFormatter

withResolverFields

​(

Set

<

TemporalField

> resolverFields)

Returns a copy of this formatter with a new set of resolver fields.

DateTimeFormatter

withResolverStyle

​(

ResolverStyle

resolverStyle)

Returns a copy of this formatter with a new resolver style.

DateTimeFormatter

withZone

​(

ZoneId

zone)

Returns a copy of this formatter with a new override zone.

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

wait

,

wait

,

wait

---

#### Method Summary

Formats a date-time object using this formatter.

Formats a date-time object to an

Appendable

using this formatter.

Gets the overriding chronology to be used during formatting.

Gets the DecimalStyle to be used during formatting.

Gets the locale to be used during formatting.

Gets the resolver fields to use during parsing.

Gets the resolver style to use during parsing.

Gets the overriding zone to be used during formatting.

Returns a copy of this formatter with localized values of the locale,
calendar, region, decimal style and/or timezone, that supercede values in
this formatter.

Returns a locale specific date format for the ISO chronology.

Returns a locale specific date-time formatter for the ISO chronology.

Returns a locale specific date and time format for the ISO chronology.

Returns a locale specific time format for the ISO chronology.

Creates a formatter using the specified pattern.

Creates a formatter using the specified pattern and locale.

Fully parses the text producing a temporal object.

Parses the text using this formatter, providing control over the text position.

Fully parses the text producing an object of the specified type.

Fully parses the text producing an object of one of the specified types.

A query that provides access to the excess days that were parsed.

A query that provides access to whether a leap-second was parsed.

Parses the text using this formatter, without resolving the result, intended
for advanced use cases.

Returns this formatter as a

java.text.Format

instance.

Returns this formatter as a

java.text.Format

instance that will
parse using the specified query.

Returns a description of the underlying formatters.

Returns a copy of this formatter with a new override chronology.

Returns a copy of this formatter with a new DecimalStyle.

Returns a copy of this formatter with a new locale.

Returns a copy of this formatter with a new set of resolver fields.

Returns a copy of this formatter with a new resolver style.

Returns a copy of this formatter with a new override zone.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- ISO_LOCAL_DATE

```java
public static final
DateTimeFormatter
ISO_LOCAL_DATE
```

The ISO date formatter that formats or parses a date without an
offset, such as '2011-12-03'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

A dash

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_OFFSET_DATE

```java
public static final
DateTimeFormatter
ISO_OFFSET_DATE
```

The ISO date formatter that formats or parses a date with an
offset, such as '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date format.
The format consists of:

- The

ISO_LOCAL_DATE

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_DATE

```java
public static final
DateTimeFormatter
ISO_DATE
```

The ISO date formatter that formats or parses a date with the
offset if available, such as '2011-12-03' or '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended date format.
The format consists of:

- The

ISO_LOCAL_DATE

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_LOCAL_TIME

```java
public static final
DateTimeFormatter
ISO_LOCAL_TIME
```

The ISO time formatter that formats or parses a time without an
offset, such as '10:15' or '10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local time format.
The format consists of:

- Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then the format is complete.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

If the nano-of-second is zero or not available then the format is complete.

A decimal point

One to nine digits for the

nano-of-second

.
As many digits will be output as required.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

- ISO_OFFSET_TIME

```java
public static final
DateTimeFormatter
ISO_OFFSET_TIME
```

The ISO time formatter that formats or parses a time with an
offset, such as '10:15+01:00' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

- ISO_TIME

```java
public static final
DateTimeFormatter
ISO_TIME
```

The ISO time formatter that formats or parses a time, with the
offset if available, such as '10:15', '10:15:30' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

- ISO_LOCAL_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_LOCAL_DATE_TIME
```

The ISO date-time formatter that formats or parses a date-time without
an offset, such as '2011-12-03T10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE

The letter 'T'. Parsing is case insensitive.

The

ISO_LOCAL_TIME

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_OFFSET_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_OFFSET_DATE_TIME
```

The ISO date-time formatter that formats or parses a date-time with an
offset, such as '2011-12-03T10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_ZONED_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_ZONED_DATE_TIME
```

The ISO-like date-time formatter that formats or parses a date-time with
offset and zone, such as '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
a format that extends the ISO-8601 extended offset date-time format
to add the time-zone.
The section in square brackets is not part of the ISO-8601 standard.
The format consists of:

- The

ISO_OFFSET_DATE_TIME

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_DATE_TIME
```

The ISO-like date-time formatter that formats or parses a date-time with
the offset and zone if available, such as '2011-12-03T10:15:30',
'2011-12-03T10:15:30+01:00' or '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local or offset date-time format, as well as the
extended non-ISO form specifying the time-zone.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_ORDINAL_DATE

```java
public static final
DateTimeFormatter
ISO_ORDINAL_DATE
```

The ISO date formatter that formats or parses the ordinal date
without an offset, such as '2012-337'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended ordinal date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Three digits for the

day-of-year

.
This is pre-padded by zero to ensure three digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_WEEK_DATE

```java
public static final
DateTimeFormatter
ISO_WEEK_DATE
```

The ISO date formatter that formats or parses the week-based date
without an offset, such as '2012-W48-6'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended week-based date format.
The format consists of:

- Four digits or more for the

week-based-year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

The letter 'W'. Parsing is case insensitive.

Two digits for the

week-of-week-based-year

.
This is pre-padded by zero to ensure three digits.

A dash

One digit for the

day-of-week

.
The value run from Monday (1) to Sunday (7).

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_INSTANT

```java
public static final
DateTimeFormatter
ISO_INSTANT
```

The ISO instant formatter that formats or parses an instant in UTC,
such as '2011-12-03T10:15:30Z'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 instant format.
When formatting, the second-of-minute is always output.
The nano-of-second outputs zero, three, six or nine digits as necessary.
When parsing, time to at least the seconds field is required.
Fractional seconds from zero to nine are parsed.
The localized decimal style is not used.

This is a special case formatter intended to allow a human readable form
of an

Instant

. The

Instant

class is designed to
only represent a point in time and internally stores a value in nanoseconds
from a fixed epoch of 1970-01-01Z. As such, an

Instant

cannot be
formatted as a date or time without providing some form of time-zone.
This formatter allows the

Instant

to be formatted, by providing
a suitable conversion using

ZoneOffset.UTC

.

The format consists of:

- The

ISO_OFFSET_DATE_TIME

where the instant is converted from

ChronoField.INSTANT_SECONDS

and

ChronoField.NANO_OF_SECOND

using the

UTC

offset. Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

- BASIC_ISO_DATE

```java
public static final
DateTimeFormatter
BASIC_ISO_DATE
```

The ISO date formatter that formats or parses a date without an
offset, such as '20111203'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 basic local date format.
The format consists of:

- Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

without colons. If the offset has
seconds then they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- RFC_1123_DATE_TIME

```java
public static final
DateTimeFormatter
RFC_1123_DATE_TIME
```

The RFC-1123 date-time formatter, such as 'Tue, 3 Jun 2008 11:05:30 GMT'.

This returns an immutable formatter capable of formatting and parsing
most of the RFC-1123 format.
RFC-1123 updates RFC-822 changing the year from two digits to four.
This implementation requires a four digit year.
This implementation also does not handle North American or military zone
names, only 'GMT' and offset amounts.

The format consists of:

- If the day-of-week is not available to format or parse then jump to day-of-month.

Three letter

day-of-week

in English.

A comma

A space

One or two digits for the

day-of-month

.

A space

Three letter

month-of-year

in English.

A space

Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

A space

Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then jump to the next space.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

A space

The

offset ID

without colons or seconds.
An offset of zero uses "GMT". North American zone names and military zone names are not handled.

Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

============ METHOD DETAIL ==========

- Method Detail

- ofPattern

```java
public static
DateTimeFormatter
ofPattern​(
String
pattern)
```

Creates a formatter using the specified pattern.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the

default FORMAT locale

.
This can be changed using

withLocale(Locale)

on the returned formatter.
Alternatively use the

ofPattern(String, Locale)

variant of this method.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

**Parameters:** pattern

- the pattern to use, not null
**Returns:** the formatter based on the pattern, not null
**Throws:** IllegalArgumentException

- if the pattern is invalid
**See Also:** DateTimeFormatterBuilder.appendPattern(String)

- ofPattern

```java
public static
DateTimeFormatter
ofPattern​(
String
pattern,

Locale
locale)
```

Creates a formatter using the specified pattern and locale.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the specified locale.
This can be changed using

withLocale(Locale)

on the returned formatter.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

**Parameters:** pattern

- the pattern to use, not null
**Parameters:** locale

- the locale to use, not null
**Returns:** the formatter based on the pattern, not null
**Throws:** IllegalArgumentException

- if the pattern is invalid
**See Also:** DateTimeFormatterBuilder.appendPattern(String)

- ofLocalizedDate

```java
public static
DateTimeFormatter
ofLocalizedDate​(
FormatStyle
dateStyle)
```

Returns a locale specific date format for the ISO chronology.

This returns a formatter that will format or parse a date.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

**Parameters:** dateStyle

- the formatter style to obtain, not null
**Returns:** the date formatter, not null

- ofLocalizedTime

```java
public static
DateTimeFormatter
ofLocalizedTime​(
FormatStyle
timeStyle)
```

Returns a locale specific time format for the ISO chronology.

This returns a formatter that will format or parse a time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:** timeStyle

- the formatter style to obtain, not null
**Returns:** the time formatter, not null

- ofLocalizedDateTime

```java
public static
DateTimeFormatter
ofLocalizedDateTime​(
FormatStyle
dateTimeStyle)
```

Returns a locale specific date-time formatter for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:** dateTimeStyle

- the formatter style to obtain, not null
**Returns:** the date-time formatter, not null

- ofLocalizedDateTime

```java
public static
DateTimeFormatter
ofLocalizedDateTime​(
FormatStyle
dateStyle,

FormatStyle
timeStyle)
```

Returns a locale specific date and time format for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:** dateStyle

- the date formatter style to obtain, not null
**Parameters:** timeStyle

- the time formatter style to obtain, not null
**Returns:** the date, time or date-time formatter, not null

- parsedExcessDays

```java
public static final
TemporalQuery
<
Period
> parsedExcessDays()
```

A query that provides access to the excess days that were parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null period, with a zero period returned instead of null.

There are two situations where this query may return a non-zero period.

- If the

ResolverStyle

is

LENIENT

and a time is parsed
without a date, then the complete result of the parse consists of a

LocalTime

and an excess

Period

in days.

If the

ResolverStyle

is

SMART

and a time is parsed
without a date where the time is 24:00:00, then the complete result of
the parse consists of a

LocalTime

of 00:00:00 and an excess

Period

of one day.

In both cases, if a complete

ChronoLocalDateTime

or

Instant

is parsed, then the excess days are added to the date part.
As a result, this query will return a zero period.

The

SMART

behaviour handles the common "end of day" 24:00 value.
Processing in

LENIENT

mode also produces the same result:

```java
Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)
```

The query can be used as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());
```

**Returns:** a query that provides access to the excess days that were parsed

- parsedLeapSecond

```java
public static final
TemporalQuery
<
Boolean
> parsedLeapSecond()
```

A query that provides access to whether a leap-second was parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null boolean, true if parsing saw a leap-second, false if not.

Instant parsing handles the special "leap second" time of '23:59:60'.
Leap seconds occur at '23:59:60' in the UTC time-zone, but at other
local times in different time-zones. To avoid this potential ambiguity,
the handling of leap-seconds is limited to

DateTimeFormatterBuilder.appendInstant()

, as that method
always parses the instant with the UTC zone offset.

If the time '23:59:60' is received, then a simple conversion is applied,
replacing the second-of-minute of 60 with 59. This query can be used
on the parse result to determine if the leap-second adjustment was made.
The query will return

true

if it did adjust to remove the
leap-second, and

false

if not. Note that applying a leap-second
smoothing mechanism, such as UTC-SLS, is the responsibility of the
application, as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
Instant instant = parsed.query(Instant::from);
if (parsed.query(DateTimeFormatter.parsedLeapSecond())) {
// validate leap-second is correct and apply correct smoothing
}
```

**Returns:** a query that provides access to whether a leap-second was parsed

- getLocale

```java
public
Locale
getLocale()
```

Gets the locale to be used during formatting.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

**Returns:** the locale of this formatter, not null

- withLocale

```java
public
DateTimeFormatter
withLocale​(
Locale
locale)
```

Returns a copy of this formatter with a new locale.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

The locale is stored as passed in, without further processing.
If the locale has

Unicode extensions

, they may be used later in text
processing. To set the chronology, time-zone and decimal style from
unicode extensions, see

localizedBy()

.

This instance is immutable and unaffected by this method call.

**Parameters:** locale

- the new locale, not null
**Returns:** a formatter based on this formatter with the requested locale, not null
**See Also:** localizedBy(Locale)

- localizedBy

```java
public
DateTimeFormatter
localizedBy​(
Locale
locale)
```

Returns a copy of this formatter with localized values of the locale,
calendar, region, decimal style and/or timezone, that supercede values in
this formatter.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern. If the locale contains the
"ca" (calendar), "nu" (numbering system), "rg" (region override), and/or
"tz" (timezone)

Unicode extensions

,
the chronology, numbering system and/or the zone are overridden. If both "ca"
and "rg" are specified, the chronology from the "ca" extension supersedes the
implicit one from the "rg" extension. Same is true for the "nu" extension.

Unlike the

withLocale

method, the call to this method may
produce a different formatter depending on the order of method chaining with
other withXXXX() methods.

This instance is immutable and unaffected by this method call.

**Parameters:** locale

- the locale, not null
**Returns:** a formatter based on this formatter with localized values of
the calendar, decimal style and/or timezone, that supercede values in this
formatter.
**Since:** 10
**See Also:** withLocale(Locale)

- getDecimalStyle

```java
public
DecimalStyle
getDecimalStyle()
```

Gets the DecimalStyle to be used during formatting.

**Returns:** the locale of this formatter, not null

- withDecimalStyle

```java
public
DateTimeFormatter
withDecimalStyle​(
DecimalStyle
decimalStyle)
```

Returns a copy of this formatter with a new DecimalStyle.

This instance is immutable and unaffected by this method call.

**Parameters:** decimalStyle

- the new DecimalStyle, not null
**Returns:** a formatter based on this formatter with the requested DecimalStyle, not null

- getChronology

```java
public
Chronology
getChronology()
```

Gets the overriding chronology to be used during formatting.

This returns the override chronology, used to convert dates.
By default, a formatter has no override chronology, returning null.
See

withChronology(Chronology)

for more details on overriding.

**Returns:** the override chronology of this formatter, null if no override

- withChronology

```java
public
DateTimeFormatter
withChronology​(
Chronology
chrono)
```

Returns a copy of this formatter with a new override chronology.

This returns a formatter with similar state to this formatter but
with the override chronology set.
By default, a formatter has no override chronology, returning null.

If an override is added, then any date that is formatted or parsed will be affected.

When formatting, if the temporal object contains a date, then it will
be converted to a date in the override chronology.
Whether the temporal contains a date is determined by querying the

EPOCH_DAY

field.
Any time or zone will be retained unaltered unless overridden.

If the temporal object does not contain a date, but does contain one
or more

ChronoField

date fields, then a

DateTimeException

is thrown. In all other cases, the override chronology is added to the temporal,
replacing any previous chronology, but without changing the date/time.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

**Parameters:** chrono

- the new chronology, null if no override
**Returns:** a formatter based on this formatter with the requested override chronology, not null

- getZone

```java
public
ZoneId
getZone()
```

Gets the overriding zone to be used during formatting.

This returns the override zone, used to convert instants.
By default, a formatter has no override zone, returning null.
See

withZone(ZoneId)

for more details on overriding.

**Returns:** the override zone of this formatter, null if no override

- withZone

```java
public
DateTimeFormatter
withZone​(
ZoneId
zone)
```

Returns a copy of this formatter with a new override zone.

This returns a formatter with similar state to this formatter but
with the override zone set.
By default, a formatter has no override zone, returning null.

If an override is added, then any instant that is formatted or parsed will be affected.

When formatting, if the temporal object contains an instant, then it will
be converted to a zoned date-time using the override zone.
Whether the temporal is an instant is determined by querying the

INSTANT_SECONDS

field.
If the input has a chronology then it will be retained unless overridden.
If the input does not have a chronology, such as

Instant

, then
the ISO chronology will be used.

If the temporal object does not contain an instant, but does contain
an offset then an additional check is made. If the normalized override
zone is an offset that differs from the offset of the temporal, then
a

DateTimeException

is thrown. In all other cases, the override
zone is added to the temporal, replacing any previous zone, but without
changing the date/time.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

**Parameters:** zone

- the new override zone, null if no override
**Returns:** a formatter based on this formatter with the requested override zone, not null

- getResolverStyle

```java
public
ResolverStyle
getResolverStyle()
```

Gets the resolver style to use during parsing.

This returns the resolver style, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has the

SMART

resolver style.
See

withResolverStyle(ResolverStyle)

for more details.

**Returns:** the resolver style of this formatter, not null

- withResolverStyle

```java
public
DateTimeFormatter
withResolverStyle​(
ResolverStyle
resolverStyle)
```

Returns a copy of this formatter with a new resolver style.

This returns a formatter with similar state to this formatter but
with the resolver style set. By default, a formatter has the

SMART

resolver style.

Changing the resolver style only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver style is used to control how phase 2, resolving, happens.
See

ResolverStyle

for more information on the options available.

This instance is immutable and unaffected by this method call.

**Parameters:** resolverStyle

- the new resolver style, not null
**Returns:** a formatter based on this formatter with the requested resolver style, not null

- getResolverFields

```java
public
Set
<
TemporalField
> getResolverFields()
```

Gets the resolver fields to use during parsing.

This returns the resolver fields, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has no resolver fields, and thus returns null.
See

withResolverFields(Set)

for more details.

**Returns:** the immutable set of resolver fields of this formatter, null if no fields

- withResolverFields

```java
public
DateTimeFormatter
withResolverFields​(
TemporalField
... resolverFields)
```

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

**Parameters:** resolverFields

- the new set of resolver fields, null if no fields
**Returns:** a formatter based on this formatter with the requested resolver style, not null

- withResolverFields

```java
public
DateTimeFormatter
withResolverFields​(
Set
<
TemporalField
> resolverFields)
```

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

**Parameters:** resolverFields

- the new set of resolver fields, null if no fields
**Returns:** a formatter based on this formatter with the requested resolver style, not null

- format

```java
public
String
format​(
TemporalAccessor
temporal)
```

Formats a date-time object using this formatter.

This formats the date-time to a String using the rules of the formatter.

**Parameters:** temporal

- the temporal object to format, not null
**Returns:** the formatted string, not null
**Throws:** DateTimeException

- if an error occurs during formatting

- formatTo

```java
public void formatTo​(
TemporalAccessor
temporal,

Appendable
appendable)
```

Formats a date-time object to an

Appendable

using this formatter.

This outputs the formatted date-time to the specified destination.

Appendable

is a general purpose interface that is implemented by all
key character output classes including

StringBuffer

,

StringBuilder

,

PrintStream

and

Writer

.

Although

Appendable

methods throw an

IOException

, this method does not.
Instead, any

IOException

is wrapped in a runtime exception.

**Parameters:** temporal

- the temporal object to format, not null
**Parameters:** appendable

- the appendable to format to, not null
**Throws:** DateTimeException

- if an error occurs during formatting

- parse

```java
public
TemporalAccessor
parse​(
CharSequence
text)
```

Fully parses the text producing a temporal object.

This parses the entire text producing a temporal object.
It is typically more useful to use

parse(CharSequence, TemporalQuery)

.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Parameters:** text

- the text to parse, not null
**Returns:** the parsed temporal object, not null
**Throws:** DateTimeParseException

- if unable to parse the requested result

- parse

```java
public
TemporalAccessor
parse​(
CharSequence
text,

ParsePosition
position)
```

Parses the text using this formatter, providing control over the text position.

This parses the text without requiring the parse to start from the beginning
of the string or finish at the end.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

The operation of this method is slightly different to similar methods using

ParsePosition

on

java.text.Format

. That class will return
errors using the error index on the

ParsePosition

. By contrast, this
method will throw a

DateTimeParseException

if an error occurs, with
the exception containing the error index.
This change in behavior is necessary due to the increased complexity of
parsing and resolving dates/times in this API.

If the formatter parses the same field more than once with different values,
the result will be an error.

**Parameters:** text

- the text to parse, not null
**Parameters:** position

- the position to parse from, updated with length parsed
and the index of any error, not null
**Returns:** the parsed temporal object, not null
**Throws:** DateTimeParseException

- if unable to parse the requested result
**Throws:** IndexOutOfBoundsException

- if the position is invalid

- parse

```java
public <T> T parse​(
CharSequence
text,

TemporalQuery
<T> query)
```

Fully parses the text producing an object of the specified type.

Most applications should use this method for parsing.
It parses the entire text to produce the required date-time.
The query is typically a method reference to a

from(TemporalAccessor)

method.
For example:

```java
LocalDateTime dt = parser.parse(str, LocalDateTime::from);
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Type Parameters:** T

- the type of the parsed date-time
**Parameters:** text

- the text to parse, not null
**Parameters:** query

- the query defining the type to parse to, not null
**Returns:** the parsed date-time, not null
**Throws:** DateTimeParseException

- if unable to parse the requested result

- parseBest

```java
public
TemporalAccessor
parseBest​(
CharSequence
text,

TemporalQuery
<?>... queries)
```

Fully parses the text producing an object of one of the specified types.

This parse method is convenient for use when the parser can handle optional elements.
For example, a pattern of 'uuuu-MM-dd HH.mm[ VV]' can be fully parsed to a

ZonedDateTime

,
or partially parsed to a

LocalDateTime

.
The queries must be specified in order, starting from the best matching full-parse option
and ending with the worst matching minimal parse option.
The query is typically a method reference to a

from(TemporalAccessor)

method.

The result is associated with the first type that successfully parses.
Normally, applications will use

instanceof

to check the result.
For example:

```java
TemporalAccessor dt = parser.parseBest(str, ZonedDateTime::from, LocalDateTime::from);
if (dt instanceof ZonedDateTime) {
...
} else {
...
}
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Parameters:** text

- the text to parse, not null
**Parameters:** queries

- the queries defining the types to attempt to parse to,
must implement

TemporalAccessor

, not null
**Returns:** the parsed date-time, not null
**Throws:** IllegalArgumentException

- if less than 2 types are specified
**Throws:** DateTimeParseException

- if unable to parse the requested result

- parseUnresolved

```java
public
TemporalAccessor
parseUnresolved​(
CharSequence
text,

ParsePosition
position)
```

Parses the text using this formatter, without resolving the result, intended
for advanced use cases.

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.
This method performs the parsing stage but not the resolving stage.

The result of this method is

TemporalAccessor

which represents the
data as seen in the input. Values are not validated, thus parsing a date string
of '2012-00-65' would result in a temporal with three fields - year of '2012',
month of '0' and day-of-month of '65'.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

Errors are returned using the error index field of the

ParsePosition

instead of

DateTimeParseException

.
The returned error index will be set to an index indicative of the error.
Callers must check for errors before using the result.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

**Parameters:** text

- the text to parse, not null
**Parameters:** position

- the position to parse from, updated with length parsed
and the index of any error, not null
**Returns:** the parsed text, null if the parse results in an error
**Throws:** DateTimeException

- if some problem occurs during parsing
**Throws:** IndexOutOfBoundsException

- if the position is invalid

- toFormat

```java
public
Format
toFormat()
```

Returns this formatter as a

java.text.Format

instance.

The returned

Format

instance will format any

TemporalAccessor

and parses to a resolved

TemporalAccessor

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

**Returns:** this formatter as a classic format instance, not null

- toFormat

```java
public
Format
toFormat​(
TemporalQuery
<?> parseQuery)
```

Returns this formatter as a

java.text.Format

instance that will
parse using the specified query.

The returned

Format

instance will format any

TemporalAccessor

and parses to the type specified.
The type must be one that is supported by

parse(java.lang.CharSequence)

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

**Parameters:** parseQuery

- the query defining the type to parse to, not null
**Returns:** this formatter as a classic format instance, not null

- toString

```java
public
String
toString()
```

Returns a description of the underlying formatters.

**Overrides:** toString

in class

Object
**Returns:** a description of this formatter, not null

Field Detail

- ISO_LOCAL_DATE

```java
public static final
DateTimeFormatter
ISO_LOCAL_DATE
```

The ISO date formatter that formats or parses a date without an
offset, such as '2011-12-03'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

A dash

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_OFFSET_DATE

```java
public static final
DateTimeFormatter
ISO_OFFSET_DATE
```

The ISO date formatter that formats or parses a date with an
offset, such as '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date format.
The format consists of:

- The

ISO_LOCAL_DATE

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_DATE

```java
public static final
DateTimeFormatter
ISO_DATE
```

The ISO date formatter that formats or parses a date with the
offset if available, such as '2011-12-03' or '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended date format.
The format consists of:

- The

ISO_LOCAL_DATE

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_LOCAL_TIME

```java
public static final
DateTimeFormatter
ISO_LOCAL_TIME
```

The ISO time formatter that formats or parses a time without an
offset, such as '10:15' or '10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local time format.
The format consists of:

- Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then the format is complete.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

If the nano-of-second is zero or not available then the format is complete.

A decimal point

One to nine digits for the

nano-of-second

.
As many digits will be output as required.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

- ISO_OFFSET_TIME

```java
public static final
DateTimeFormatter
ISO_OFFSET_TIME
```

The ISO time formatter that formats or parses a time with an
offset, such as '10:15+01:00' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

- ISO_TIME

```java
public static final
DateTimeFormatter
ISO_TIME
```

The ISO time formatter that formats or parses a time, with the
offset if available, such as '10:15', '10:15:30' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

- ISO_LOCAL_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_LOCAL_DATE_TIME
```

The ISO date-time formatter that formats or parses a date-time without
an offset, such as '2011-12-03T10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE

The letter 'T'. Parsing is case insensitive.

The

ISO_LOCAL_TIME

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_OFFSET_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_OFFSET_DATE_TIME
```

The ISO date-time formatter that formats or parses a date-time with an
offset, such as '2011-12-03T10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_ZONED_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_ZONED_DATE_TIME
```

The ISO-like date-time formatter that formats or parses a date-time with
offset and zone, such as '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
a format that extends the ISO-8601 extended offset date-time format
to add the time-zone.
The section in square brackets is not part of the ISO-8601 standard.
The format consists of:

- The

ISO_OFFSET_DATE_TIME

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_DATE_TIME
```

The ISO-like date-time formatter that formats or parses a date-time with
the offset and zone if available, such as '2011-12-03T10:15:30',
'2011-12-03T10:15:30+01:00' or '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local or offset date-time format, as well as the
extended non-ISO form specifying the time-zone.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_ORDINAL_DATE

```java
public static final
DateTimeFormatter
ISO_ORDINAL_DATE
```

The ISO date formatter that formats or parses the ordinal date
without an offset, such as '2012-337'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended ordinal date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Three digits for the

day-of-year

.
This is pre-padded by zero to ensure three digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_WEEK_DATE

```java
public static final
DateTimeFormatter
ISO_WEEK_DATE
```

The ISO date formatter that formats or parses the week-based date
without an offset, such as '2012-W48-6'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended week-based date format.
The format consists of:

- Four digits or more for the

week-based-year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

The letter 'W'. Parsing is case insensitive.

Two digits for the

week-of-week-based-year

.
This is pre-padded by zero to ensure three digits.

A dash

One digit for the

day-of-week

.
The value run from Monday (1) to Sunday (7).

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- ISO_INSTANT

```java
public static final
DateTimeFormatter
ISO_INSTANT
```

The ISO instant formatter that formats or parses an instant in UTC,
such as '2011-12-03T10:15:30Z'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 instant format.
When formatting, the second-of-minute is always output.
The nano-of-second outputs zero, three, six or nine digits as necessary.
When parsing, time to at least the seconds field is required.
Fractional seconds from zero to nine are parsed.
The localized decimal style is not used.

This is a special case formatter intended to allow a human readable form
of an

Instant

. The

Instant

class is designed to
only represent a point in time and internally stores a value in nanoseconds
from a fixed epoch of 1970-01-01Z. As such, an

Instant

cannot be
formatted as a date or time without providing some form of time-zone.
This formatter allows the

Instant

to be formatted, by providing
a suitable conversion using

ZoneOffset.UTC

.

The format consists of:

- The

ISO_OFFSET_DATE_TIME

where the instant is converted from

ChronoField.INSTANT_SECONDS

and

ChronoField.NANO_OF_SECOND

using the

UTC

offset. Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

- BASIC_ISO_DATE

```java
public static final
DateTimeFormatter
BASIC_ISO_DATE
```

The ISO date formatter that formats or parses a date without an
offset, such as '20111203'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 basic local date format.
The format consists of:

- Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

without colons. If the offset has
seconds then they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

- RFC_1123_DATE_TIME

```java
public static final
DateTimeFormatter
RFC_1123_DATE_TIME
```

The RFC-1123 date-time formatter, such as 'Tue, 3 Jun 2008 11:05:30 GMT'.

This returns an immutable formatter capable of formatting and parsing
most of the RFC-1123 format.
RFC-1123 updates RFC-822 changing the year from two digits to four.
This implementation requires a four digit year.
This implementation also does not handle North American or military zone
names, only 'GMT' and offset amounts.

The format consists of:

- If the day-of-week is not available to format or parse then jump to day-of-month.

Three letter

day-of-week

in English.

A comma

A space

One or two digits for the

day-of-month

.

A space

Three letter

month-of-year

in English.

A space

Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

A space

Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then jump to the next space.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

A space

The

offset ID

without colons or seconds.
An offset of zero uses "GMT". North American zone names and military zone names are not handled.

Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

---

#### Field Detail

ISO_LOCAL_DATE

```java
public static final
DateTimeFormatter
ISO_LOCAL_DATE
```

The ISO date formatter that formats or parses a date without an
offset, such as '2011-12-03'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

A dash

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### ISO_LOCAL_DATE

public static final

DateTimeFormatter

ISO_LOCAL_DATE

The ISO date formatter that formats or parses a date without an
offset, such as '2011-12-03'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

A dash

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

A dash

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

A dash

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

ISO_OFFSET_DATE

```java
public static final
DateTimeFormatter
ISO_OFFSET_DATE
```

The ISO date formatter that formats or parses a date with an
offset, such as '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date format.
The format consists of:

- The

ISO_LOCAL_DATE

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### ISO_OFFSET_DATE

public static final

DateTimeFormatter

ISO_OFFSET_DATE

The ISO date formatter that formats or parses a date with an
offset, such as '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date format.
The format consists of:

- The

ISO_LOCAL_DATE

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date format.
The format consists of:

- The

ISO_LOCAL_DATE

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The

ISO_LOCAL_DATE

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

ISO_DATE

```java
public static final
DateTimeFormatter
ISO_DATE
```

The ISO date formatter that formats or parses a date with the
offset if available, such as '2011-12-03' or '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended date format.
The format consists of:

- The

ISO_LOCAL_DATE

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### ISO_DATE

public static final

DateTimeFormatter

ISO_DATE

The ISO date formatter that formats or parses a date with the
offset if available, such as '2011-12-03' or '2011-12-03+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended date format.
The format consists of:

- The

ISO_LOCAL_DATE

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended date format.
The format consists of:

- The

ISO_LOCAL_DATE

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The

ISO_LOCAL_DATE

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

ISO_LOCAL_TIME

```java
public static final
DateTimeFormatter
ISO_LOCAL_TIME
```

The ISO time formatter that formats or parses a time without an
offset, such as '10:15' or '10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local time format.
The format consists of:

- Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then the format is complete.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

If the nano-of-second is zero or not available then the format is complete.

A decimal point

One to nine digits for the

nano-of-second

.
As many digits will be output as required.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

---

#### ISO_LOCAL_TIME

public static final

DateTimeFormatter

ISO_LOCAL_TIME

The ISO time formatter that formats or parses a time without an
offset, such as '10:15' or '10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local time format.
The format consists of:

- Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then the format is complete.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

If the nano-of-second is zero or not available then the format is complete.

A decimal point

One to nine digits for the

nano-of-second

.
As many digits will be output as required.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local time format.
The format consists of:

- Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then the format is complete.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

If the nano-of-second is zero or not available then the format is complete.

A decimal point

One to nine digits for the

nano-of-second

.
As many digits will be output as required.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then the format is complete.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

If the nano-of-second is zero or not available then the format is complete.

A decimal point

One to nine digits for the

nano-of-second

.
As many digits will be output as required.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

ISO_OFFSET_TIME

```java
public static final
DateTimeFormatter
ISO_OFFSET_TIME
```

The ISO time formatter that formats or parses a time with an
offset, such as '10:15+01:00' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

---

#### ISO_OFFSET_TIME

public static final

DateTimeFormatter

ISO_OFFSET_TIME

The ISO time formatter that formats or parses a time with an
offset, such as '10:15+01:00' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

The

ISO_LOCAL_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

ISO_TIME

```java
public static final
DateTimeFormatter
ISO_TIME
```

The ISO time formatter that formats or parses a time, with the
offset if available, such as '10:15', '10:15:30' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

---

#### ISO_TIME

public static final

DateTimeFormatter

ISO_TIME

The ISO time formatter that formats or parses a time, with the
offset if available, such as '10:15', '10:15:30' or '10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset time format.
The format consists of:

- The

ISO_LOCAL_TIME

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

The

ISO_LOCAL_TIME

If the offset is not available then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

ISO_LOCAL_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_LOCAL_DATE_TIME
```

The ISO date-time formatter that formats or parses a date-time without
an offset, such as '2011-12-03T10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE

The letter 'T'. Parsing is case insensitive.

The

ISO_LOCAL_TIME

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### ISO_LOCAL_DATE_TIME

public static final

DateTimeFormatter

ISO_LOCAL_DATE_TIME

The ISO date-time formatter that formats or parses a date-time without
an offset, such as '2011-12-03T10:15:30'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE

The letter 'T'. Parsing is case insensitive.

The

ISO_LOCAL_TIME

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE

The letter 'T'. Parsing is case insensitive.

The

ISO_LOCAL_TIME

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The

ISO_LOCAL_DATE

The letter 'T'. Parsing is case insensitive.

The

ISO_LOCAL_TIME

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

ISO_OFFSET_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_OFFSET_DATE_TIME
```

The ISO date-time formatter that formats or parses a date-time with an
offset, such as '2011-12-03T10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### ISO_OFFSET_DATE_TIME

public static final

DateTimeFormatter

ISO_OFFSET_DATE_TIME

The ISO date-time formatter that formats or parses a date-time with an
offset, such as '2011-12-03T10:15:30+01:00'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended offset date-time format.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The

ISO_LOCAL_DATE_TIME

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

ISO_ZONED_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_ZONED_DATE_TIME
```

The ISO-like date-time formatter that formats or parses a date-time with
offset and zone, such as '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
a format that extends the ISO-8601 extended offset date-time format
to add the time-zone.
The section in square brackets is not part of the ISO-8601 standard.
The format consists of:

- The

ISO_OFFSET_DATE_TIME

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### ISO_ZONED_DATE_TIME

public static final

DateTimeFormatter

ISO_ZONED_DATE_TIME

The ISO-like date-time formatter that formats or parses a date-time with
offset and zone, such as '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
a format that extends the ISO-8601 extended offset date-time format
to add the time-zone.
The section in square brackets is not part of the ISO-8601 standard.
The format consists of:

- The

ISO_OFFSET_DATE_TIME

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
a format that extends the ISO-8601 extended offset date-time format
to add the time-zone.
The section in square brackets is not part of the ISO-8601 standard.
The format consists of:

- The

ISO_OFFSET_DATE_TIME

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The

ISO_OFFSET_DATE_TIME

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

ISO_DATE_TIME

```java
public static final
DateTimeFormatter
ISO_DATE_TIME
```

The ISO-like date-time formatter that formats or parses a date-time with
the offset and zone if available, such as '2011-12-03T10:15:30',
'2011-12-03T10:15:30+01:00' or '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local or offset date-time format, as well as the
extended non-ISO form specifying the time-zone.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### ISO_DATE_TIME

public static final

DateTimeFormatter

ISO_DATE_TIME

The ISO-like date-time formatter that formats or parses a date-time with
the offset and zone if available, such as '2011-12-03T10:15:30',
'2011-12-03T10:15:30+01:00' or '2011-12-03T10:15:30+01:00[Europe/Paris]'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local or offset date-time format, as well as the
extended non-ISO form specifying the time-zone.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended local or offset date-time format, as well as the
extended non-ISO form specifying the time-zone.
The format consists of:

- The

ISO_LOCAL_DATE_TIME

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The

ISO_LOCAL_DATE_TIME

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.

If the zone ID is not available or is a

ZoneOffset

then the format is complete.

An open square bracket '['.

The

zone ID

. This is not part of the ISO-8601 standard.
Parsing is case sensitive.

A close square bracket ']'.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

ISO_ORDINAL_DATE

```java
public static final
DateTimeFormatter
ISO_ORDINAL_DATE
```

The ISO date formatter that formats or parses the ordinal date
without an offset, such as '2012-337'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended ordinal date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Three digits for the

day-of-year

.
This is pre-padded by zero to ensure three digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### ISO_ORDINAL_DATE

public static final

DateTimeFormatter

ISO_ORDINAL_DATE

The ISO date formatter that formats or parses the ordinal date
without an offset, such as '2012-337'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended ordinal date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Three digits for the

day-of-year

.
This is pre-padded by zero to ensure three digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended ordinal date format.
The format consists of:

- Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Three digits for the

day-of-year

.
This is pre-padded by zero to ensure three digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

Four digits or more for the

year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

Three digits for the

day-of-year

.
This is pre-padded by zero to ensure three digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

ISO_WEEK_DATE

```java
public static final
DateTimeFormatter
ISO_WEEK_DATE
```

The ISO date formatter that formats or parses the week-based date
without an offset, such as '2012-W48-6'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended week-based date format.
The format consists of:

- Four digits or more for the

week-based-year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

The letter 'W'. Parsing is case insensitive.

Two digits for the

week-of-week-based-year

.
This is pre-padded by zero to ensure three digits.

A dash

One digit for the

day-of-week

.
The value run from Monday (1) to Sunday (7).

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### ISO_WEEK_DATE

public static final

DateTimeFormatter

ISO_WEEK_DATE

The ISO date formatter that formats or parses the week-based date
without an offset, such as '2012-W48-6'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended week-based date format.
The format consists of:

- Four digits or more for the

week-based-year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

The letter 'W'. Parsing is case insensitive.

Two digits for the

week-of-week-based-year

.
This is pre-padded by zero to ensure three digits.

A dash

One digit for the

day-of-week

.
The value run from Monday (1) to Sunday (7).

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 extended week-based date format.
The format consists of:

- Four digits or more for the

week-based-year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

The letter 'W'. Parsing is case insensitive.

Two digits for the

week-of-week-based-year

.
This is pre-padded by zero to ensure three digits.

A dash

One digit for the

day-of-week

.
The value run from Monday (1) to Sunday (7).

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

Four digits or more for the

week-based-year

.
Years in the range 0000 to 9999 will be pre-padded by zero to ensure four digits.
Years outside that range will have a prefixed positive or negative symbol.

A dash

The letter 'W'. Parsing is case insensitive.

Two digits for the

week-of-week-based-year

.
This is pre-padded by zero to ensure three digits.

A dash

One digit for the

day-of-week

.
The value run from Monday (1) to Sunday (7).

If the offset is not available to format or parse then the format is complete.

The

offset ID

. If the offset has seconds then
they will be handled even though this is not part of the ISO-8601 standard.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

ISO_INSTANT

```java
public static final
DateTimeFormatter
ISO_INSTANT
```

The ISO instant formatter that formats or parses an instant in UTC,
such as '2011-12-03T10:15:30Z'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 instant format.
When formatting, the second-of-minute is always output.
The nano-of-second outputs zero, three, six or nine digits as necessary.
When parsing, time to at least the seconds field is required.
Fractional seconds from zero to nine are parsed.
The localized decimal style is not used.

This is a special case formatter intended to allow a human readable form
of an

Instant

. The

Instant

class is designed to
only represent a point in time and internally stores a value in nanoseconds
from a fixed epoch of 1970-01-01Z. As such, an

Instant

cannot be
formatted as a date or time without providing some form of time-zone.
This formatter allows the

Instant

to be formatted, by providing
a suitable conversion using

ZoneOffset.UTC

.

The format consists of:

- The

ISO_OFFSET_DATE_TIME

where the instant is converted from

ChronoField.INSTANT_SECONDS

and

ChronoField.NANO_OF_SECOND

using the

UTC

offset. Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

---

#### ISO_INSTANT

public static final

DateTimeFormatter

ISO_INSTANT

The ISO instant formatter that formats or parses an instant in UTC,
such as '2011-12-03T10:15:30Z'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 instant format.
When formatting, the second-of-minute is always output.
The nano-of-second outputs zero, three, six or nine digits as necessary.
When parsing, time to at least the seconds field is required.
Fractional seconds from zero to nine are parsed.
The localized decimal style is not used.

This is a special case formatter intended to allow a human readable form
of an

Instant

. The

Instant

class is designed to
only represent a point in time and internally stores a value in nanoseconds
from a fixed epoch of 1970-01-01Z. As such, an

Instant

cannot be
formatted as a date or time without providing some form of time-zone.
This formatter allows the

Instant

to be formatted, by providing
a suitable conversion using

ZoneOffset.UTC

.

The format consists of:

- The

ISO_OFFSET_DATE_TIME

where the instant is converted from

ChronoField.INSTANT_SECONDS

and

ChronoField.NANO_OF_SECOND

using the

UTC

offset. Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 instant format.
When formatting, the second-of-minute is always output.
The nano-of-second outputs zero, three, six or nine digits as necessary.
When parsing, time to at least the seconds field is required.
Fractional seconds from zero to nine are parsed.
The localized decimal style is not used.

This is a special case formatter intended to allow a human readable form
of an

Instant

. The

Instant

class is designed to
only represent a point in time and internally stores a value in nanoseconds
from a fixed epoch of 1970-01-01Z. As such, an

Instant

cannot be
formatted as a date or time without providing some form of time-zone.
This formatter allows the

Instant

to be formatted, by providing
a suitable conversion using

ZoneOffset.UTC

.

The format consists of:

- The

ISO_OFFSET_DATE_TIME

where the instant is converted from

ChronoField.INSTANT_SECONDS

and

ChronoField.NANO_OF_SECOND

using the

UTC

offset. Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

This is a special case formatter intended to allow a human readable form
of an

Instant

. The

Instant

class is designed to
only represent a point in time and internally stores a value in nanoseconds
from a fixed epoch of 1970-01-01Z. As such, an

Instant

cannot be
formatted as a date or time without providing some form of time-zone.
This formatter allows the

Instant

to be formatted, by providing
a suitable conversion using

ZoneOffset.UTC

.

The format consists of:

- The

ISO_OFFSET_DATE_TIME

where the instant is converted from

ChronoField.INSTANT_SECONDS

and

ChronoField.NANO_OF_SECOND

using the

UTC

offset. Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

The format consists of:

- The

ISO_OFFSET_DATE_TIME

where the instant is converted from

ChronoField.INSTANT_SECONDS

and

ChronoField.NANO_OF_SECOND

using the

UTC

offset. Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

The

ISO_OFFSET_DATE_TIME

where the instant is converted from

ChronoField.INSTANT_SECONDS

and

ChronoField.NANO_OF_SECOND

using the

UTC

offset. Parsing is case insensitive.

The returned formatter has no override chronology or zone.
It uses the

STRICT

resolver style.

BASIC_ISO_DATE

```java
public static final
DateTimeFormatter
BASIC_ISO_DATE
```

The ISO date formatter that formats or parses a date without an
offset, such as '20111203'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 basic local date format.
The format consists of:

- Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

without colons. If the offset has
seconds then they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

---

#### BASIC_ISO_DATE

public static final

DateTimeFormatter

BASIC_ISO_DATE

The ISO date formatter that formats or parses a date without an
offset, such as '20111203'.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 basic local date format.
The format consists of:

- Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

without colons. If the offset has
seconds then they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

This returns an immutable formatter capable of formatting and parsing
the ISO-8601 basic local date format.
The format consists of:

- Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

without colons. If the offset has
seconds then they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

Two digits for the

month-of-year

.
This is pre-padded by zero to ensure two digits.

Two digits for the

day-of-month

.
This is pre-padded by zero to ensure two digits.

If the offset is not available to format or parse then the format is complete.

The

offset ID

without colons. If the offset has
seconds then they will be handled even though this is not part of the ISO-8601 standard.
The offset parsing is lenient, which allows the minutes and seconds to be optional.
Parsing is case insensitive.

As this formatter has an optional element, it may be necessary to parse using

parseBest(java.lang.CharSequence, java.time.temporal.TemporalQuery<?>...)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

STRICT

resolver style.

RFC_1123_DATE_TIME

```java
public static final
DateTimeFormatter
RFC_1123_DATE_TIME
```

The RFC-1123 date-time formatter, such as 'Tue, 3 Jun 2008 11:05:30 GMT'.

This returns an immutable formatter capable of formatting and parsing
most of the RFC-1123 format.
RFC-1123 updates RFC-822 changing the year from two digits to four.
This implementation requires a four digit year.
This implementation also does not handle North American or military zone
names, only 'GMT' and offset amounts.

The format consists of:

- If the day-of-week is not available to format or parse then jump to day-of-month.

Three letter

day-of-week

in English.

A comma

A space

One or two digits for the

day-of-month

.

A space

Three letter

month-of-year

in English.

A space

Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

A space

Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then jump to the next space.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

A space

The

offset ID

without colons or seconds.
An offset of zero uses "GMT". North American zone names and military zone names are not handled.

Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

---

#### RFC_1123_DATE_TIME

public static final

DateTimeFormatter

RFC_1123_DATE_TIME

The RFC-1123 date-time formatter, such as 'Tue, 3 Jun 2008 11:05:30 GMT'.

This returns an immutable formatter capable of formatting and parsing
most of the RFC-1123 format.
RFC-1123 updates RFC-822 changing the year from two digits to four.
This implementation requires a four digit year.
This implementation also does not handle North American or military zone
names, only 'GMT' and offset amounts.

The format consists of:

- If the day-of-week is not available to format or parse then jump to day-of-month.

Three letter

day-of-week

in English.

A comma

A space

One or two digits for the

day-of-month

.

A space

Three letter

month-of-year

in English.

A space

Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

A space

Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then jump to the next space.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

A space

The

offset ID

without colons or seconds.
An offset of zero uses "GMT". North American zone names and military zone names are not handled.

Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

This returns an immutable formatter capable of formatting and parsing
most of the RFC-1123 format.
RFC-1123 updates RFC-822 changing the year from two digits to four.
This implementation requires a four digit year.
This implementation also does not handle North American or military zone
names, only 'GMT' and offset amounts.

The format consists of:

- If the day-of-week is not available to format or parse then jump to day-of-month.

Three letter

day-of-week

in English.

A comma

A space

One or two digits for the

day-of-month

.

A space

Three letter

month-of-year

in English.

A space

Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

A space

Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then jump to the next space.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

A space

The

offset ID

without colons or seconds.
An offset of zero uses "GMT". North American zone names and military zone names are not handled.

Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

The format consists of:

- If the day-of-week is not available to format or parse then jump to day-of-month.

Three letter

day-of-week

in English.

A comma

A space

One or two digits for the

day-of-month

.

A space

Three letter

month-of-year

in English.

A space

Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

A space

Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then jump to the next space.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

A space

The

offset ID

without colons or seconds.
An offset of zero uses "GMT". North American zone names and military zone names are not handled.

Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

If the day-of-week is not available to format or parse then jump to day-of-month.

Three letter

day-of-week

in English.

A comma

A space

One or two digits for the

day-of-month

.

A space

Three letter

month-of-year

in English.

A space

Four digits for the

year

.
Only years in the range 0000 to 9999 are supported.

A space

Two digits for the

hour-of-day

.
This is pre-padded by zero to ensure two digits.

A colon

Two digits for the

minute-of-hour

.
This is pre-padded by zero to ensure two digits.

If the second-of-minute is not available then jump to the next space.

A colon

Two digits for the

second-of-minute

.
This is pre-padded by zero to ensure two digits.

A space

The

offset ID

without colons or seconds.
An offset of zero uses "GMT". North American zone names and military zone names are not handled.

Parsing is case insensitive.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

Method Detail

- ofPattern

```java
public static
DateTimeFormatter
ofPattern​(
String
pattern)
```

Creates a formatter using the specified pattern.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the

default FORMAT locale

.
This can be changed using

withLocale(Locale)

on the returned formatter.
Alternatively use the

ofPattern(String, Locale)

variant of this method.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

**Parameters:** pattern

- the pattern to use, not null
**Returns:** the formatter based on the pattern, not null
**Throws:** IllegalArgumentException

- if the pattern is invalid
**See Also:** DateTimeFormatterBuilder.appendPattern(String)

- ofPattern

```java
public static
DateTimeFormatter
ofPattern​(
String
pattern,

Locale
locale)
```

Creates a formatter using the specified pattern and locale.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the specified locale.
This can be changed using

withLocale(Locale)

on the returned formatter.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

**Parameters:** pattern

- the pattern to use, not null
**Parameters:** locale

- the locale to use, not null
**Returns:** the formatter based on the pattern, not null
**Throws:** IllegalArgumentException

- if the pattern is invalid
**See Also:** DateTimeFormatterBuilder.appendPattern(String)

- ofLocalizedDate

```java
public static
DateTimeFormatter
ofLocalizedDate​(
FormatStyle
dateStyle)
```

Returns a locale specific date format for the ISO chronology.

This returns a formatter that will format or parse a date.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

**Parameters:** dateStyle

- the formatter style to obtain, not null
**Returns:** the date formatter, not null

- ofLocalizedTime

```java
public static
DateTimeFormatter
ofLocalizedTime​(
FormatStyle
timeStyle)
```

Returns a locale specific time format for the ISO chronology.

This returns a formatter that will format or parse a time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:** timeStyle

- the formatter style to obtain, not null
**Returns:** the time formatter, not null

- ofLocalizedDateTime

```java
public static
DateTimeFormatter
ofLocalizedDateTime​(
FormatStyle
dateTimeStyle)
```

Returns a locale specific date-time formatter for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:** dateTimeStyle

- the formatter style to obtain, not null
**Returns:** the date-time formatter, not null

- ofLocalizedDateTime

```java
public static
DateTimeFormatter
ofLocalizedDateTime​(
FormatStyle
dateStyle,

FormatStyle
timeStyle)
```

Returns a locale specific date and time format for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:** dateStyle

- the date formatter style to obtain, not null
**Parameters:** timeStyle

- the time formatter style to obtain, not null
**Returns:** the date, time or date-time formatter, not null

- parsedExcessDays

```java
public static final
TemporalQuery
<
Period
> parsedExcessDays()
```

A query that provides access to the excess days that were parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null period, with a zero period returned instead of null.

There are two situations where this query may return a non-zero period.

- If the

ResolverStyle

is

LENIENT

and a time is parsed
without a date, then the complete result of the parse consists of a

LocalTime

and an excess

Period

in days.

If the

ResolverStyle

is

SMART

and a time is parsed
without a date where the time is 24:00:00, then the complete result of
the parse consists of a

LocalTime

of 00:00:00 and an excess

Period

of one day.

In both cases, if a complete

ChronoLocalDateTime

or

Instant

is parsed, then the excess days are added to the date part.
As a result, this query will return a zero period.

The

SMART

behaviour handles the common "end of day" 24:00 value.
Processing in

LENIENT

mode also produces the same result:

```java
Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)
```

The query can be used as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());
```

**Returns:** a query that provides access to the excess days that were parsed

- parsedLeapSecond

```java
public static final
TemporalQuery
<
Boolean
> parsedLeapSecond()
```

A query that provides access to whether a leap-second was parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null boolean, true if parsing saw a leap-second, false if not.

Instant parsing handles the special "leap second" time of '23:59:60'.
Leap seconds occur at '23:59:60' in the UTC time-zone, but at other
local times in different time-zones. To avoid this potential ambiguity,
the handling of leap-seconds is limited to

DateTimeFormatterBuilder.appendInstant()

, as that method
always parses the instant with the UTC zone offset.

If the time '23:59:60' is received, then a simple conversion is applied,
replacing the second-of-minute of 60 with 59. This query can be used
on the parse result to determine if the leap-second adjustment was made.
The query will return

true

if it did adjust to remove the
leap-second, and

false

if not. Note that applying a leap-second
smoothing mechanism, such as UTC-SLS, is the responsibility of the
application, as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
Instant instant = parsed.query(Instant::from);
if (parsed.query(DateTimeFormatter.parsedLeapSecond())) {
// validate leap-second is correct and apply correct smoothing
}
```

**Returns:** a query that provides access to whether a leap-second was parsed

- getLocale

```java
public
Locale
getLocale()
```

Gets the locale to be used during formatting.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

**Returns:** the locale of this formatter, not null

- withLocale

```java
public
DateTimeFormatter
withLocale​(
Locale
locale)
```

Returns a copy of this formatter with a new locale.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

The locale is stored as passed in, without further processing.
If the locale has

Unicode extensions

, they may be used later in text
processing. To set the chronology, time-zone and decimal style from
unicode extensions, see

localizedBy()

.

This instance is immutable and unaffected by this method call.

**Parameters:** locale

- the new locale, not null
**Returns:** a formatter based on this formatter with the requested locale, not null
**See Also:** localizedBy(Locale)

- localizedBy

```java
public
DateTimeFormatter
localizedBy​(
Locale
locale)
```

Returns a copy of this formatter with localized values of the locale,
calendar, region, decimal style and/or timezone, that supercede values in
this formatter.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern. If the locale contains the
"ca" (calendar), "nu" (numbering system), "rg" (region override), and/or
"tz" (timezone)

Unicode extensions

,
the chronology, numbering system and/or the zone are overridden. If both "ca"
and "rg" are specified, the chronology from the "ca" extension supersedes the
implicit one from the "rg" extension. Same is true for the "nu" extension.

Unlike the

withLocale

method, the call to this method may
produce a different formatter depending on the order of method chaining with
other withXXXX() methods.

This instance is immutable and unaffected by this method call.

**Parameters:** locale

- the locale, not null
**Returns:** a formatter based on this formatter with localized values of
the calendar, decimal style and/or timezone, that supercede values in this
formatter.
**Since:** 10
**See Also:** withLocale(Locale)

- getDecimalStyle

```java
public
DecimalStyle
getDecimalStyle()
```

Gets the DecimalStyle to be used during formatting.

**Returns:** the locale of this formatter, not null

- withDecimalStyle

```java
public
DateTimeFormatter
withDecimalStyle​(
DecimalStyle
decimalStyle)
```

Returns a copy of this formatter with a new DecimalStyle.

This instance is immutable and unaffected by this method call.

**Parameters:** decimalStyle

- the new DecimalStyle, not null
**Returns:** a formatter based on this formatter with the requested DecimalStyle, not null

- getChronology

```java
public
Chronology
getChronology()
```

Gets the overriding chronology to be used during formatting.

This returns the override chronology, used to convert dates.
By default, a formatter has no override chronology, returning null.
See

withChronology(Chronology)

for more details on overriding.

**Returns:** the override chronology of this formatter, null if no override

- withChronology

```java
public
DateTimeFormatter
withChronology​(
Chronology
chrono)
```

Returns a copy of this formatter with a new override chronology.

This returns a formatter with similar state to this formatter but
with the override chronology set.
By default, a formatter has no override chronology, returning null.

If an override is added, then any date that is formatted or parsed will be affected.

When formatting, if the temporal object contains a date, then it will
be converted to a date in the override chronology.
Whether the temporal contains a date is determined by querying the

EPOCH_DAY

field.
Any time or zone will be retained unaltered unless overridden.

If the temporal object does not contain a date, but does contain one
or more

ChronoField

date fields, then a

DateTimeException

is thrown. In all other cases, the override chronology is added to the temporal,
replacing any previous chronology, but without changing the date/time.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

**Parameters:** chrono

- the new chronology, null if no override
**Returns:** a formatter based on this formatter with the requested override chronology, not null

- getZone

```java
public
ZoneId
getZone()
```

Gets the overriding zone to be used during formatting.

This returns the override zone, used to convert instants.
By default, a formatter has no override zone, returning null.
See

withZone(ZoneId)

for more details on overriding.

**Returns:** the override zone of this formatter, null if no override

- withZone

```java
public
DateTimeFormatter
withZone​(
ZoneId
zone)
```

Returns a copy of this formatter with a new override zone.

This returns a formatter with similar state to this formatter but
with the override zone set.
By default, a formatter has no override zone, returning null.

If an override is added, then any instant that is formatted or parsed will be affected.

When formatting, if the temporal object contains an instant, then it will
be converted to a zoned date-time using the override zone.
Whether the temporal is an instant is determined by querying the

INSTANT_SECONDS

field.
If the input has a chronology then it will be retained unless overridden.
If the input does not have a chronology, such as

Instant

, then
the ISO chronology will be used.

If the temporal object does not contain an instant, but does contain
an offset then an additional check is made. If the normalized override
zone is an offset that differs from the offset of the temporal, then
a

DateTimeException

is thrown. In all other cases, the override
zone is added to the temporal, replacing any previous zone, but without
changing the date/time.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

**Parameters:** zone

- the new override zone, null if no override
**Returns:** a formatter based on this formatter with the requested override zone, not null

- getResolverStyle

```java
public
ResolverStyle
getResolverStyle()
```

Gets the resolver style to use during parsing.

This returns the resolver style, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has the

SMART

resolver style.
See

withResolverStyle(ResolverStyle)

for more details.

**Returns:** the resolver style of this formatter, not null

- withResolverStyle

```java
public
DateTimeFormatter
withResolverStyle​(
ResolverStyle
resolverStyle)
```

Returns a copy of this formatter with a new resolver style.

This returns a formatter with similar state to this formatter but
with the resolver style set. By default, a formatter has the

SMART

resolver style.

Changing the resolver style only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver style is used to control how phase 2, resolving, happens.
See

ResolverStyle

for more information on the options available.

This instance is immutable and unaffected by this method call.

**Parameters:** resolverStyle

- the new resolver style, not null
**Returns:** a formatter based on this formatter with the requested resolver style, not null

- getResolverFields

```java
public
Set
<
TemporalField
> getResolverFields()
```

Gets the resolver fields to use during parsing.

This returns the resolver fields, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has no resolver fields, and thus returns null.
See

withResolverFields(Set)

for more details.

**Returns:** the immutable set of resolver fields of this formatter, null if no fields

- withResolverFields

```java
public
DateTimeFormatter
withResolverFields​(
TemporalField
... resolverFields)
```

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

**Parameters:** resolverFields

- the new set of resolver fields, null if no fields
**Returns:** a formatter based on this formatter with the requested resolver style, not null

- withResolverFields

```java
public
DateTimeFormatter
withResolverFields​(
Set
<
TemporalField
> resolverFields)
```

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

**Parameters:** resolverFields

- the new set of resolver fields, null if no fields
**Returns:** a formatter based on this formatter with the requested resolver style, not null

- format

```java
public
String
format​(
TemporalAccessor
temporal)
```

Formats a date-time object using this formatter.

This formats the date-time to a String using the rules of the formatter.

**Parameters:** temporal

- the temporal object to format, not null
**Returns:** the formatted string, not null
**Throws:** DateTimeException

- if an error occurs during formatting

- formatTo

```java
public void formatTo​(
TemporalAccessor
temporal,

Appendable
appendable)
```

Formats a date-time object to an

Appendable

using this formatter.

This outputs the formatted date-time to the specified destination.

Appendable

is a general purpose interface that is implemented by all
key character output classes including

StringBuffer

,

StringBuilder

,

PrintStream

and

Writer

.

Although

Appendable

methods throw an

IOException

, this method does not.
Instead, any

IOException

is wrapped in a runtime exception.

**Parameters:** temporal

- the temporal object to format, not null
**Parameters:** appendable

- the appendable to format to, not null
**Throws:** DateTimeException

- if an error occurs during formatting

- parse

```java
public
TemporalAccessor
parse​(
CharSequence
text)
```

Fully parses the text producing a temporal object.

This parses the entire text producing a temporal object.
It is typically more useful to use

parse(CharSequence, TemporalQuery)

.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Parameters:** text

- the text to parse, not null
**Returns:** the parsed temporal object, not null
**Throws:** DateTimeParseException

- if unable to parse the requested result

- parse

```java
public
TemporalAccessor
parse​(
CharSequence
text,

ParsePosition
position)
```

Parses the text using this formatter, providing control over the text position.

This parses the text without requiring the parse to start from the beginning
of the string or finish at the end.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

The operation of this method is slightly different to similar methods using

ParsePosition

on

java.text.Format

. That class will return
errors using the error index on the

ParsePosition

. By contrast, this
method will throw a

DateTimeParseException

if an error occurs, with
the exception containing the error index.
This change in behavior is necessary due to the increased complexity of
parsing and resolving dates/times in this API.

If the formatter parses the same field more than once with different values,
the result will be an error.

**Parameters:** text

- the text to parse, not null
**Parameters:** position

- the position to parse from, updated with length parsed
and the index of any error, not null
**Returns:** the parsed temporal object, not null
**Throws:** DateTimeParseException

- if unable to parse the requested result
**Throws:** IndexOutOfBoundsException

- if the position is invalid

- parse

```java
public <T> T parse​(
CharSequence
text,

TemporalQuery
<T> query)
```

Fully parses the text producing an object of the specified type.

Most applications should use this method for parsing.
It parses the entire text to produce the required date-time.
The query is typically a method reference to a

from(TemporalAccessor)

method.
For example:

```java
LocalDateTime dt = parser.parse(str, LocalDateTime::from);
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Type Parameters:** T

- the type of the parsed date-time
**Parameters:** text

- the text to parse, not null
**Parameters:** query

- the query defining the type to parse to, not null
**Returns:** the parsed date-time, not null
**Throws:** DateTimeParseException

- if unable to parse the requested result

- parseBest

```java
public
TemporalAccessor
parseBest​(
CharSequence
text,

TemporalQuery
<?>... queries)
```

Fully parses the text producing an object of one of the specified types.

This parse method is convenient for use when the parser can handle optional elements.
For example, a pattern of 'uuuu-MM-dd HH.mm[ VV]' can be fully parsed to a

ZonedDateTime

,
or partially parsed to a

LocalDateTime

.
The queries must be specified in order, starting from the best matching full-parse option
and ending with the worst matching minimal parse option.
The query is typically a method reference to a

from(TemporalAccessor)

method.

The result is associated with the first type that successfully parses.
Normally, applications will use

instanceof

to check the result.
For example:

```java
TemporalAccessor dt = parser.parseBest(str, ZonedDateTime::from, LocalDateTime::from);
if (dt instanceof ZonedDateTime) {
...
} else {
...
}
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Parameters:** text

- the text to parse, not null
**Parameters:** queries

- the queries defining the types to attempt to parse to,
must implement

TemporalAccessor

, not null
**Returns:** the parsed date-time, not null
**Throws:** IllegalArgumentException

- if less than 2 types are specified
**Throws:** DateTimeParseException

- if unable to parse the requested result

- parseUnresolved

```java
public
TemporalAccessor
parseUnresolved​(
CharSequence
text,

ParsePosition
position)
```

Parses the text using this formatter, without resolving the result, intended
for advanced use cases.

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.
This method performs the parsing stage but not the resolving stage.

The result of this method is

TemporalAccessor

which represents the
data as seen in the input. Values are not validated, thus parsing a date string
of '2012-00-65' would result in a temporal with three fields - year of '2012',
month of '0' and day-of-month of '65'.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

Errors are returned using the error index field of the

ParsePosition

instead of

DateTimeParseException

.
The returned error index will be set to an index indicative of the error.
Callers must check for errors before using the result.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

**Parameters:** text

- the text to parse, not null
**Parameters:** position

- the position to parse from, updated with length parsed
and the index of any error, not null
**Returns:** the parsed text, null if the parse results in an error
**Throws:** DateTimeException

- if some problem occurs during parsing
**Throws:** IndexOutOfBoundsException

- if the position is invalid

- toFormat

```java
public
Format
toFormat()
```

Returns this formatter as a

java.text.Format

instance.

The returned

Format

instance will format any

TemporalAccessor

and parses to a resolved

TemporalAccessor

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

**Returns:** this formatter as a classic format instance, not null

- toFormat

```java
public
Format
toFormat​(
TemporalQuery
<?> parseQuery)
```

Returns this formatter as a

java.text.Format

instance that will
parse using the specified query.

The returned

Format

instance will format any

TemporalAccessor

and parses to the type specified.
The type must be one that is supported by

parse(java.lang.CharSequence)

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

**Parameters:** parseQuery

- the query defining the type to parse to, not null
**Returns:** this formatter as a classic format instance, not null

- toString

```java
public
String
toString()
```

Returns a description of the underlying formatters.

**Overrides:** toString

in class

Object
**Returns:** a description of this formatter, not null

---

#### Method Detail

ofPattern

```java
public static
DateTimeFormatter
ofPattern​(
String
pattern)
```

Creates a formatter using the specified pattern.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the

default FORMAT locale

.
This can be changed using

withLocale(Locale)

on the returned formatter.
Alternatively use the

ofPattern(String, Locale)

variant of this method.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

**Parameters:** pattern

- the pattern to use, not null
**Returns:** the formatter based on the pattern, not null
**Throws:** IllegalArgumentException

- if the pattern is invalid
**See Also:** DateTimeFormatterBuilder.appendPattern(String)

---

#### ofPattern

public static

DateTimeFormatter

ofPattern​(

String

pattern)

Creates a formatter using the specified pattern.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the

default FORMAT locale

.
This can be changed using

withLocale(Locale)

on the returned formatter.
Alternatively use the

ofPattern(String, Locale)

variant of this method.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the

default FORMAT locale

.
This can be changed using

withLocale(Locale)

on the returned formatter.
Alternatively use the

ofPattern(String, Locale)

variant of this method.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

The formatter will use the

default FORMAT locale

.
This can be changed using

withLocale(Locale)

on the returned formatter.
Alternatively use the

ofPattern(String, Locale)

variant of this method.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

ofPattern

```java
public static
DateTimeFormatter
ofPattern​(
String
pattern,

Locale
locale)
```

Creates a formatter using the specified pattern and locale.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the specified locale.
This can be changed using

withLocale(Locale)

on the returned formatter.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

**Parameters:** pattern

- the pattern to use, not null
**Parameters:** locale

- the locale to use, not null
**Returns:** the formatter based on the pattern, not null
**Throws:** IllegalArgumentException

- if the pattern is invalid
**See Also:** DateTimeFormatterBuilder.appendPattern(String)

---

#### ofPattern

public static

DateTimeFormatter

ofPattern​(

String

pattern,

Locale

locale)

Creates a formatter using the specified pattern and locale.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the specified locale.
This can be changed using

withLocale(Locale)

on the returned formatter.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

This method will create a formatter based on a simple

pattern of letters and symbols

as described in the class documentation.
For example,

d MMM uuuu

will format 2011-12-03 as '3 Dec 2011'.

The formatter will use the specified locale.
This can be changed using

withLocale(Locale)

on the returned formatter.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

The formatter will use the specified locale.
This can be changed using

withLocale(Locale)

on the returned formatter.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

The returned formatter has no override chronology or zone.
It uses

SMART

resolver style.

ofLocalizedDate

```java
public static
DateTimeFormatter
ofLocalizedDate​(
FormatStyle
dateStyle)
```

Returns a locale specific date format for the ISO chronology.

This returns a formatter that will format or parse a date.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

**Parameters:** dateStyle

- the formatter style to obtain, not null
**Returns:** the date formatter, not null

---

#### ofLocalizedDate

public static

DateTimeFormatter

ofLocalizedDate​(

FormatStyle

dateStyle)

Returns a locale specific date format for the ISO chronology.

This returns a formatter that will format or parse a date.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

This returns a formatter that will format or parse a date.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.

ofLocalizedTime

```java
public static
DateTimeFormatter
ofLocalizedTime​(
FormatStyle
timeStyle)
```

Returns a locale specific time format for the ISO chronology.

This returns a formatter that will format or parse a time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:** timeStyle

- the formatter style to obtain, not null
**Returns:** the time formatter, not null

---

#### ofLocalizedTime

public static

DateTimeFormatter

ofLocalizedTime​(

FormatStyle

timeStyle)

Returns a locale specific time format for the ISO chronology.

This returns a formatter that will format or parse a time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

This returns a formatter that will format or parse a time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

ofLocalizedDateTime

```java
public static
DateTimeFormatter
ofLocalizedDateTime​(
FormatStyle
dateTimeStyle)
```

Returns a locale specific date-time formatter for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:** dateTimeStyle

- the formatter style to obtain, not null
**Returns:** the date-time formatter, not null

---

#### ofLocalizedDateTime

public static

DateTimeFormatter

ofLocalizedDateTime​(

FormatStyle

dateTimeStyle)

Returns a locale specific date-time formatter for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

ofLocalizedDateTime

```java
public static
DateTimeFormatter
ofLocalizedDateTime​(
FormatStyle
dateStyle,

FormatStyle
timeStyle)
```

Returns a locale specific date and time format for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

**Parameters:** dateStyle

- the date formatter style to obtain, not null
**Parameters:** timeStyle

- the time formatter style to obtain, not null
**Returns:** the date, time or date-time formatter, not null

---

#### ofLocalizedDateTime

public static

DateTimeFormatter

ofLocalizedDateTime​(

FormatStyle

dateStyle,

FormatStyle

timeStyle)

Returns a locale specific date and time format for the ISO chronology.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

This returns a formatter that will format or parse a date-time.
The exact format pattern used varies by locale.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

The locale is determined from the formatter. The formatter returned directly by
this method will use the

default FORMAT locale

.
The locale can be controlled using

withLocale(Locale)

on the result of this method.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

Note that the localized pattern is looked up lazily.
This

DateTimeFormatter

holds the style required and the locale,
looking up the pattern required on demand.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

The returned formatter has a chronology of ISO set to ensure dates in
other calendar systems are correctly converted.
It has no override zone and uses the

SMART

resolver style.
The

FULL

and

LONG

styles typically require a time-zone.
When formatting using these styles, a

ZoneId

must be available,
either by using

ZonedDateTime

or

withZone(java.time.ZoneId)

.

parsedExcessDays

```java
public static final
TemporalQuery
<
Period
> parsedExcessDays()
```

A query that provides access to the excess days that were parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null period, with a zero period returned instead of null.

There are two situations where this query may return a non-zero period.

- If the

ResolverStyle

is

LENIENT

and a time is parsed
without a date, then the complete result of the parse consists of a

LocalTime

and an excess

Period

in days.

If the

ResolverStyle

is

SMART

and a time is parsed
without a date where the time is 24:00:00, then the complete result of
the parse consists of a

LocalTime

of 00:00:00 and an excess

Period

of one day.

In both cases, if a complete

ChronoLocalDateTime

or

Instant

is parsed, then the excess days are added to the date part.
As a result, this query will return a zero period.

The

SMART

behaviour handles the common "end of day" 24:00 value.
Processing in

LENIENT

mode also produces the same result:

```java
Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)
```

The query can be used as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());
```

**Returns:** a query that provides access to the excess days that were parsed

---

#### parsedExcessDays

public static final

TemporalQuery

<

Period

> parsedExcessDays()

A query that provides access to the excess days that were parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null period, with a zero period returned instead of null.

There are two situations where this query may return a non-zero period.

- If the

ResolverStyle

is

LENIENT

and a time is parsed
without a date, then the complete result of the parse consists of a

LocalTime

and an excess

Period

in days.

If the

ResolverStyle

is

SMART

and a time is parsed
without a date where the time is 24:00:00, then the complete result of
the parse consists of a

LocalTime

of 00:00:00 and an excess

Period

of one day.

In both cases, if a complete

ChronoLocalDateTime

or

Instant

is parsed, then the excess days are added to the date part.
As a result, this query will return a zero period.

The

SMART

behaviour handles the common "end of day" 24:00 value.
Processing in

LENIENT

mode also produces the same result:

```java
Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)
```

The query can be used as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());
```

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null period, with a zero period returned instead of null.

There are two situations where this query may return a non-zero period.

- If the

ResolverStyle

is

LENIENT

and a time is parsed
without a date, then the complete result of the parse consists of a

LocalTime

and an excess

Period

in days.

If the

ResolverStyle

is

SMART

and a time is parsed
without a date where the time is 24:00:00, then the complete result of
the parse consists of a

LocalTime

of 00:00:00 and an excess

Period

of one day.

In both cases, if a complete

ChronoLocalDateTime

or

Instant

is parsed, then the excess days are added to the date part.
As a result, this query will return a zero period.

The

SMART

behaviour handles the common "end of day" 24:00 value.
Processing in

LENIENT

mode also produces the same result:

```java
Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)
```

The query can be used as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());
```

There are two situations where this query may return a non-zero period.

- If the

ResolverStyle

is

LENIENT

and a time is parsed
without a date, then the complete result of the parse consists of a

LocalTime

and an excess

Period

in days.

If the

ResolverStyle

is

SMART

and a time is parsed
without a date where the time is 24:00:00, then the complete result of
the parse consists of a

LocalTime

of 00:00:00 and an excess

Period

of one day.

In both cases, if a complete

ChronoLocalDateTime

or

Instant

is parsed, then the excess days are added to the date part.
As a result, this query will return a zero period.

The

SMART

behaviour handles the common "end of day" 24:00 value.
Processing in

LENIENT

mode also produces the same result:

```java
Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)
```

The query can be used as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());
```

If the

ResolverStyle

is

LENIENT

and a time is parsed
without a date, then the complete result of the parse consists of a

LocalTime

and an excess

Period

in days.

If the

ResolverStyle

is

SMART

and a time is parsed
without a date where the time is 24:00:00, then the complete result of
the parse consists of a

LocalTime

of 00:00:00 and an excess

Period

of one day.

In both cases, if a complete

ChronoLocalDateTime

or

Instant

is parsed, then the excess days are added to the date part.
As a result, this query will return a zero period.

The

SMART

behaviour handles the common "end of day" 24:00 value.
Processing in

LENIENT

mode also produces the same result:

```java
Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)
```

The query can be used as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());
```

The

SMART

behaviour handles the common "end of day" 24:00 value.
Processing in

LENIENT

mode also produces the same result:

```java
Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)
```

The query can be used as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());
```

Text to parse Parsed object Excess days
"2012-12-03T00:00" LocalDateTime.of(2012, 12, 3, 0, 0) ZERO
"2012-12-03T24:00" LocalDateTime.of(2012, 12, 4, 0, 0) ZERO
"00:00" LocalTime.of(0, 0) ZERO
"24:00" LocalTime.of(0, 0) Period.ofDays(1)

TemporalAccessor parsed = formatter.parse(str);
LocalTime time = parsed.query(LocalTime::from);
Period extraDays = parsed.query(DateTimeFormatter.parsedExcessDays());

parsedLeapSecond

```java
public static final
TemporalQuery
<
Boolean
> parsedLeapSecond()
```

A query that provides access to whether a leap-second was parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null boolean, true if parsing saw a leap-second, false if not.

Instant parsing handles the special "leap second" time of '23:59:60'.
Leap seconds occur at '23:59:60' in the UTC time-zone, but at other
local times in different time-zones. To avoid this potential ambiguity,
the handling of leap-seconds is limited to

DateTimeFormatterBuilder.appendInstant()

, as that method
always parses the instant with the UTC zone offset.

If the time '23:59:60' is received, then a simple conversion is applied,
replacing the second-of-minute of 60 with 59. This query can be used
on the parse result to determine if the leap-second adjustment was made.
The query will return

true

if it did adjust to remove the
leap-second, and

false

if not. Note that applying a leap-second
smoothing mechanism, such as UTC-SLS, is the responsibility of the
application, as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
Instant instant = parsed.query(Instant::from);
if (parsed.query(DateTimeFormatter.parsedLeapSecond())) {
// validate leap-second is correct and apply correct smoothing
}
```

**Returns:** a query that provides access to whether a leap-second was parsed

---

#### parsedLeapSecond

public static final

TemporalQuery

<

Boolean

> parsedLeapSecond()

A query that provides access to whether a leap-second was parsed.

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null boolean, true if parsing saw a leap-second, false if not.

Instant parsing handles the special "leap second" time of '23:59:60'.
Leap seconds occur at '23:59:60' in the UTC time-zone, but at other
local times in different time-zones. To avoid this potential ambiguity,
the handling of leap-seconds is limited to

DateTimeFormatterBuilder.appendInstant()

, as that method
always parses the instant with the UTC zone offset.

If the time '23:59:60' is received, then a simple conversion is applied,
replacing the second-of-minute of 60 with 59. This query can be used
on the parse result to determine if the leap-second adjustment was made.
The query will return

true

if it did adjust to remove the
leap-second, and

false

if not. Note that applying a leap-second
smoothing mechanism, such as UTC-SLS, is the responsibility of the
application, as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
Instant instant = parsed.query(Instant::from);
if (parsed.query(DateTimeFormatter.parsedLeapSecond())) {
// validate leap-second is correct and apply correct smoothing
}
```

This returns a singleton

query

that provides
access to additional information from the parse. The query always returns
a non-null boolean, true if parsing saw a leap-second, false if not.

Instant parsing handles the special "leap second" time of '23:59:60'.
Leap seconds occur at '23:59:60' in the UTC time-zone, but at other
local times in different time-zones. To avoid this potential ambiguity,
the handling of leap-seconds is limited to

DateTimeFormatterBuilder.appendInstant()

, as that method
always parses the instant with the UTC zone offset.

If the time '23:59:60' is received, then a simple conversion is applied,
replacing the second-of-minute of 60 with 59. This query can be used
on the parse result to determine if the leap-second adjustment was made.
The query will return

true

if it did adjust to remove the
leap-second, and

false

if not. Note that applying a leap-second
smoothing mechanism, such as UTC-SLS, is the responsibility of the
application, as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
Instant instant = parsed.query(Instant::from);
if (parsed.query(DateTimeFormatter.parsedLeapSecond())) {
// validate leap-second is correct and apply correct smoothing
}
```

Instant parsing handles the special "leap second" time of '23:59:60'.
Leap seconds occur at '23:59:60' in the UTC time-zone, but at other
local times in different time-zones. To avoid this potential ambiguity,
the handling of leap-seconds is limited to

DateTimeFormatterBuilder.appendInstant()

, as that method
always parses the instant with the UTC zone offset.

If the time '23:59:60' is received, then a simple conversion is applied,
replacing the second-of-minute of 60 with 59. This query can be used
on the parse result to determine if the leap-second adjustment was made.
The query will return

true

if it did adjust to remove the
leap-second, and

false

if not. Note that applying a leap-second
smoothing mechanism, such as UTC-SLS, is the responsibility of the
application, as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
Instant instant = parsed.query(Instant::from);
if (parsed.query(DateTimeFormatter.parsedLeapSecond())) {
// validate leap-second is correct and apply correct smoothing
}
```

If the time '23:59:60' is received, then a simple conversion is applied,
replacing the second-of-minute of 60 with 59. This query can be used
on the parse result to determine if the leap-second adjustment was made.
The query will return

true

if it did adjust to remove the
leap-second, and

false

if not. Note that applying a leap-second
smoothing mechanism, such as UTC-SLS, is the responsibility of the
application, as follows:

```java
TemporalAccessor parsed = formatter.parse(str);
Instant instant = parsed.query(Instant::from);
if (parsed.query(DateTimeFormatter.parsedLeapSecond())) {
// validate leap-second is correct and apply correct smoothing
}
```

TemporalAccessor parsed = formatter.parse(str);
Instant instant = parsed.query(Instant::from);
if (parsed.query(DateTimeFormatter.parsedLeapSecond())) {
// validate leap-second is correct and apply correct smoothing
}

getLocale

```java
public
Locale
getLocale()
```

Gets the locale to be used during formatting.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

**Returns:** the locale of this formatter, not null

---

#### getLocale

public

Locale

getLocale()

Gets the locale to be used during formatting.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

withLocale

```java
public
DateTimeFormatter
withLocale​(
Locale
locale)
```

Returns a copy of this formatter with a new locale.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

The locale is stored as passed in, without further processing.
If the locale has

Unicode extensions

, they may be used later in text
processing. To set the chronology, time-zone and decimal style from
unicode extensions, see

localizedBy()

.

This instance is immutable and unaffected by this method call.

**Parameters:** locale

- the new locale, not null
**Returns:** a formatter based on this formatter with the requested locale, not null
**See Also:** localizedBy(Locale)

---

#### withLocale

public

DateTimeFormatter

withLocale​(

Locale

locale)

Returns a copy of this formatter with a new locale.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

The locale is stored as passed in, without further processing.
If the locale has

Unicode extensions

, they may be used later in text
processing. To set the chronology, time-zone and decimal style from
unicode extensions, see

localizedBy()

.

This instance is immutable and unaffected by this method call.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern.

The locale is stored as passed in, without further processing.
If the locale has

Unicode extensions

, they may be used later in text
processing. To set the chronology, time-zone and decimal style from
unicode extensions, see

localizedBy()

.

This instance is immutable and unaffected by this method call.

The locale is stored as passed in, without further processing.
If the locale has

Unicode extensions

, they may be used later in text
processing. To set the chronology, time-zone and decimal style from
unicode extensions, see

localizedBy()

.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

localizedBy

```java
public
DateTimeFormatter
localizedBy​(
Locale
locale)
```

Returns a copy of this formatter with localized values of the locale,
calendar, region, decimal style and/or timezone, that supercede values in
this formatter.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern. If the locale contains the
"ca" (calendar), "nu" (numbering system), "rg" (region override), and/or
"tz" (timezone)

Unicode extensions

,
the chronology, numbering system and/or the zone are overridden. If both "ca"
and "rg" are specified, the chronology from the "ca" extension supersedes the
implicit one from the "rg" extension. Same is true for the "nu" extension.

Unlike the

withLocale

method, the call to this method may
produce a different formatter depending on the order of method chaining with
other withXXXX() methods.

This instance is immutable and unaffected by this method call.

**Parameters:** locale

- the locale, not null
**Returns:** a formatter based on this formatter with localized values of
the calendar, decimal style and/or timezone, that supercede values in this
formatter.
**Since:** 10
**See Also:** withLocale(Locale)

---

#### localizedBy

public

DateTimeFormatter

localizedBy​(

Locale

locale)

Returns a copy of this formatter with localized values of the locale,
calendar, region, decimal style and/or timezone, that supercede values in
this formatter.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern. If the locale contains the
"ca" (calendar), "nu" (numbering system), "rg" (region override), and/or
"tz" (timezone)

Unicode extensions

,
the chronology, numbering system and/or the zone are overridden. If both "ca"
and "rg" are specified, the chronology from the "ca" extension supersedes the
implicit one from the "rg" extension. Same is true for the "nu" extension.

Unlike the

withLocale

method, the call to this method may
produce a different formatter depending on the order of method chaining with
other withXXXX() methods.

This instance is immutable and unaffected by this method call.

This is used to lookup any part of the formatter needing specific
localization, such as the text or localized pattern. If the locale contains the
"ca" (calendar), "nu" (numbering system), "rg" (region override), and/or
"tz" (timezone)

Unicode extensions

,
the chronology, numbering system and/or the zone are overridden. If both "ca"
and "rg" are specified, the chronology from the "ca" extension supersedes the
implicit one from the "rg" extension. Same is true for the "nu" extension.

Unlike the

withLocale

method, the call to this method may
produce a different formatter depending on the order of method chaining with
other withXXXX() methods.

This instance is immutable and unaffected by this method call.

Unlike the

withLocale

method, the call to this method may
produce a different formatter depending on the order of method chaining with
other withXXXX() methods.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

getDecimalStyle

```java
public
DecimalStyle
getDecimalStyle()
```

Gets the DecimalStyle to be used during formatting.

**Returns:** the locale of this formatter, not null

---

#### getDecimalStyle

public

DecimalStyle

getDecimalStyle()

Gets the DecimalStyle to be used during formatting.

withDecimalStyle

```java
public
DateTimeFormatter
withDecimalStyle​(
DecimalStyle
decimalStyle)
```

Returns a copy of this formatter with a new DecimalStyle.

This instance is immutable and unaffected by this method call.

**Parameters:** decimalStyle

- the new DecimalStyle, not null
**Returns:** a formatter based on this formatter with the requested DecimalStyle, not null

---

#### withDecimalStyle

public

DateTimeFormatter

withDecimalStyle​(

DecimalStyle

decimalStyle)

Returns a copy of this formatter with a new DecimalStyle.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

getChronology

```java
public
Chronology
getChronology()
```

Gets the overriding chronology to be used during formatting.

This returns the override chronology, used to convert dates.
By default, a formatter has no override chronology, returning null.
See

withChronology(Chronology)

for more details on overriding.

**Returns:** the override chronology of this formatter, null if no override

---

#### getChronology

public

Chronology

getChronology()

Gets the overriding chronology to be used during formatting.

This returns the override chronology, used to convert dates.
By default, a formatter has no override chronology, returning null.
See

withChronology(Chronology)

for more details on overriding.

This returns the override chronology, used to convert dates.
By default, a formatter has no override chronology, returning null.
See

withChronology(Chronology)

for more details on overriding.

withChronology

```java
public
DateTimeFormatter
withChronology​(
Chronology
chrono)
```

Returns a copy of this formatter with a new override chronology.

This returns a formatter with similar state to this formatter but
with the override chronology set.
By default, a formatter has no override chronology, returning null.

If an override is added, then any date that is formatted or parsed will be affected.

When formatting, if the temporal object contains a date, then it will
be converted to a date in the override chronology.
Whether the temporal contains a date is determined by querying the

EPOCH_DAY

field.
Any time or zone will be retained unaltered unless overridden.

If the temporal object does not contain a date, but does contain one
or more

ChronoField

date fields, then a

DateTimeException

is thrown. In all other cases, the override chronology is added to the temporal,
replacing any previous chronology, but without changing the date/time.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

**Parameters:** chrono

- the new chronology, null if no override
**Returns:** a formatter based on this formatter with the requested override chronology, not null

---

#### withChronology

public

DateTimeFormatter

withChronology​(

Chronology

chrono)

Returns a copy of this formatter with a new override chronology.

This returns a formatter with similar state to this formatter but
with the override chronology set.
By default, a formatter has no override chronology, returning null.

If an override is added, then any date that is formatted or parsed will be affected.

When formatting, if the temporal object contains a date, then it will
be converted to a date in the override chronology.
Whether the temporal contains a date is determined by querying the

EPOCH_DAY

field.
Any time or zone will be retained unaltered unless overridden.

If the temporal object does not contain a date, but does contain one
or more

ChronoField

date fields, then a

DateTimeException

is thrown. In all other cases, the override chronology is added to the temporal,
replacing any previous chronology, but without changing the date/time.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

This returns a formatter with similar state to this formatter but
with the override chronology set.
By default, a formatter has no override chronology, returning null.

If an override is added, then any date that is formatted or parsed will be affected.

When formatting, if the temporal object contains a date, then it will
be converted to a date in the override chronology.
Whether the temporal contains a date is determined by querying the

EPOCH_DAY

field.
Any time or zone will be retained unaltered unless overridden.

If the temporal object does not contain a date, but does contain one
or more

ChronoField

date fields, then a

DateTimeException

is thrown. In all other cases, the override chronology is added to the temporal,
replacing any previous chronology, but without changing the date/time.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

If an override is added, then any date that is formatted or parsed will be affected.

When formatting, if the temporal object contains a date, then it will
be converted to a date in the override chronology.
Whether the temporal contains a date is determined by querying the

EPOCH_DAY

field.
Any time or zone will be retained unaltered unless overridden.

If the temporal object does not contain a date, but does contain one
or more

ChronoField

date fields, then a

DateTimeException

is thrown. In all other cases, the override chronology is added to the temporal,
replacing any previous chronology, but without changing the date/time.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

When formatting, if the temporal object contains a date, then it will
be converted to a date in the override chronology.
Whether the temporal contains a date is determined by querying the

EPOCH_DAY

field.
Any time or zone will be retained unaltered unless overridden.

If the temporal object does not contain a date, but does contain one
or more

ChronoField

date fields, then a

DateTimeException

is thrown. In all other cases, the override chronology is added to the temporal,
replacing any previous chronology, but without changing the date/time.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

If the temporal object does not contain a date, but does contain one
or more

ChronoField

date fields, then a

DateTimeException

is thrown. In all other cases, the override chronology is added to the temporal,
replacing any previous chronology, but without changing the date/time.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

When parsing, there are two distinct cases to consider.
If a chronology has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendChronologyId()

was used, then
this override chronology has no effect.
If no zone has been parsed, then this override chronology will be used
to interpret the

ChronoField

values into a date according to the
date resolving rules of the chronology.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

getZone

```java
public
ZoneId
getZone()
```

Gets the overriding zone to be used during formatting.

This returns the override zone, used to convert instants.
By default, a formatter has no override zone, returning null.
See

withZone(ZoneId)

for more details on overriding.

**Returns:** the override zone of this formatter, null if no override

---

#### getZone

public

ZoneId

getZone()

Gets the overriding zone to be used during formatting.

This returns the override zone, used to convert instants.
By default, a formatter has no override zone, returning null.
See

withZone(ZoneId)

for more details on overriding.

This returns the override zone, used to convert instants.
By default, a formatter has no override zone, returning null.
See

withZone(ZoneId)

for more details on overriding.

withZone

```java
public
DateTimeFormatter
withZone​(
ZoneId
zone)
```

Returns a copy of this formatter with a new override zone.

This returns a formatter with similar state to this formatter but
with the override zone set.
By default, a formatter has no override zone, returning null.

If an override is added, then any instant that is formatted or parsed will be affected.

When formatting, if the temporal object contains an instant, then it will
be converted to a zoned date-time using the override zone.
Whether the temporal is an instant is determined by querying the

INSTANT_SECONDS

field.
If the input has a chronology then it will be retained unless overridden.
If the input does not have a chronology, such as

Instant

, then
the ISO chronology will be used.

If the temporal object does not contain an instant, but does contain
an offset then an additional check is made. If the normalized override
zone is an offset that differs from the offset of the temporal, then
a

DateTimeException

is thrown. In all other cases, the override
zone is added to the temporal, replacing any previous zone, but without
changing the date/time.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

**Parameters:** zone

- the new override zone, null if no override
**Returns:** a formatter based on this formatter with the requested override zone, not null

---

#### withZone

public

DateTimeFormatter

withZone​(

ZoneId

zone)

Returns a copy of this formatter with a new override zone.

This returns a formatter with similar state to this formatter but
with the override zone set.
By default, a formatter has no override zone, returning null.

If an override is added, then any instant that is formatted or parsed will be affected.

When formatting, if the temporal object contains an instant, then it will
be converted to a zoned date-time using the override zone.
Whether the temporal is an instant is determined by querying the

INSTANT_SECONDS

field.
If the input has a chronology then it will be retained unless overridden.
If the input does not have a chronology, such as

Instant

, then
the ISO chronology will be used.

If the temporal object does not contain an instant, but does contain
an offset then an additional check is made. If the normalized override
zone is an offset that differs from the offset of the temporal, then
a

DateTimeException

is thrown. In all other cases, the override
zone is added to the temporal, replacing any previous zone, but without
changing the date/time.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

This returns a formatter with similar state to this formatter but
with the override zone set.
By default, a formatter has no override zone, returning null.

If an override is added, then any instant that is formatted or parsed will be affected.

When formatting, if the temporal object contains an instant, then it will
be converted to a zoned date-time using the override zone.
Whether the temporal is an instant is determined by querying the

INSTANT_SECONDS

field.
If the input has a chronology then it will be retained unless overridden.
If the input does not have a chronology, such as

Instant

, then
the ISO chronology will be used.

If the temporal object does not contain an instant, but does contain
an offset then an additional check is made. If the normalized override
zone is an offset that differs from the offset of the temporal, then
a

DateTimeException

is thrown. In all other cases, the override
zone is added to the temporal, replacing any previous zone, but without
changing the date/time.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

If an override is added, then any instant that is formatted or parsed will be affected.

When formatting, if the temporal object contains an instant, then it will
be converted to a zoned date-time using the override zone.
Whether the temporal is an instant is determined by querying the

INSTANT_SECONDS

field.
If the input has a chronology then it will be retained unless overridden.
If the input does not have a chronology, such as

Instant

, then
the ISO chronology will be used.

If the temporal object does not contain an instant, but does contain
an offset then an additional check is made. If the normalized override
zone is an offset that differs from the offset of the temporal, then
a

DateTimeException

is thrown. In all other cases, the override
zone is added to the temporal, replacing any previous zone, but without
changing the date/time.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

When formatting, if the temporal object contains an instant, then it will
be converted to a zoned date-time using the override zone.
Whether the temporal is an instant is determined by querying the

INSTANT_SECONDS

field.
If the input has a chronology then it will be retained unless overridden.
If the input does not have a chronology, such as

Instant

, then
the ISO chronology will be used.

If the temporal object does not contain an instant, but does contain
an offset then an additional check is made. If the normalized override
zone is an offset that differs from the offset of the temporal, then
a

DateTimeException

is thrown. In all other cases, the override
zone is added to the temporal, replacing any previous zone, but without
changing the date/time.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

If the temporal object does not contain an instant, but does contain
an offset then an additional check is made. If the normalized override
zone is an offset that differs from the offset of the temporal, then
a

DateTimeException

is thrown. In all other cases, the override
zone is added to the temporal, replacing any previous zone, but without
changing the date/time.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

When parsing, there are two distinct cases to consider.
If a zone has been parsed directly from the text, perhaps because

DateTimeFormatterBuilder.appendZoneId()

was used, then
this override zone has no effect.
If no zone has been parsed, then this override zone will be included in
the result of the parse where it can be used to build instants and date-times.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

getResolverStyle

```java
public
ResolverStyle
getResolverStyle()
```

Gets the resolver style to use during parsing.

This returns the resolver style, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has the

SMART

resolver style.
See

withResolverStyle(ResolverStyle)

for more details.

**Returns:** the resolver style of this formatter, not null

---

#### getResolverStyle

public

ResolverStyle

getResolverStyle()

Gets the resolver style to use during parsing.

This returns the resolver style, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has the

SMART

resolver style.
See

withResolverStyle(ResolverStyle)

for more details.

This returns the resolver style, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has the

SMART

resolver style.
See

withResolverStyle(ResolverStyle)

for more details.

withResolverStyle

```java
public
DateTimeFormatter
withResolverStyle​(
ResolverStyle
resolverStyle)
```

Returns a copy of this formatter with a new resolver style.

This returns a formatter with similar state to this formatter but
with the resolver style set. By default, a formatter has the

SMART

resolver style.

Changing the resolver style only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver style is used to control how phase 2, resolving, happens.
See

ResolverStyle

for more information on the options available.

This instance is immutable and unaffected by this method call.

**Parameters:** resolverStyle

- the new resolver style, not null
**Returns:** a formatter based on this formatter with the requested resolver style, not null

---

#### withResolverStyle

public

DateTimeFormatter

withResolverStyle​(

ResolverStyle

resolverStyle)

Returns a copy of this formatter with a new resolver style.

This returns a formatter with similar state to this formatter but
with the resolver style set. By default, a formatter has the

SMART

resolver style.

Changing the resolver style only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver style is used to control how phase 2, resolving, happens.
See

ResolverStyle

for more information on the options available.

This instance is immutable and unaffected by this method call.

This returns a formatter with similar state to this formatter but
with the resolver style set. By default, a formatter has the

SMART

resolver style.

Changing the resolver style only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver style is used to control how phase 2, resolving, happens.
See

ResolverStyle

for more information on the options available.

This instance is immutable and unaffected by this method call.

Changing the resolver style only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver style is used to control how phase 2, resolving, happens.
See

ResolverStyle

for more information on the options available.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

getResolverFields

```java
public
Set
<
TemporalField
> getResolverFields()
```

Gets the resolver fields to use during parsing.

This returns the resolver fields, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has no resolver fields, and thus returns null.
See

withResolverFields(Set)

for more details.

**Returns:** the immutable set of resolver fields of this formatter, null if no fields

---

#### getResolverFields

public

Set

<

TemporalField

> getResolverFields()

Gets the resolver fields to use during parsing.

This returns the resolver fields, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has no resolver fields, and thus returns null.
See

withResolverFields(Set)

for more details.

This returns the resolver fields, used during the second phase of parsing
when fields are resolved into dates and times.
By default, a formatter has no resolver fields, and thus returns null.
See

withResolverFields(Set)

for more details.

withResolverFields

```java
public
DateTimeFormatter
withResolverFields​(
TemporalField
... resolverFields)
```

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

**Parameters:** resolverFields

- the new set of resolver fields, null if no fields
**Returns:** a formatter based on this formatter with the requested resolver style, not null

---

#### withResolverFields

public

DateTimeFormatter

withResolverFields​(

TemporalField

... resolverFields)

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

withResolverFields

```java
public
DateTimeFormatter
withResolverFields​(
Set
<
TemporalField
> resolverFields)
```

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

**Parameters:** resolverFields

- the new set of resolver fields, null if no fields
**Returns:** a formatter based on this formatter with the requested resolver style, not null

---

#### withResolverFields

public

DateTimeFormatter

withResolverFields​(

Set

<

TemporalField

> resolverFields)

Returns a copy of this formatter with a new set of resolver fields.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

This returns a formatter with similar state to this formatter but with
the resolver fields set. By default, a formatter has no resolver fields.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

Changing the resolver fields only has an effect during parsing.
Parsing a text string occurs in two phases.
Phase 1 is a basic text parse according to the fields added to the builder.
Phase 2 resolves the parsed field-value pairs into date and/or time objects.
The resolver fields are used to filter the field-value pairs between phase 1 and 2.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

This can be used to select between two or more ways that a date or time might
be resolved. For example, if the formatter consists of year, month, day-of-month
and day-of-year, then there are two ways to resolve a date.
Calling this method with the arguments

YEAR

and

DAY_OF_YEAR

will ensure that the date is
resolved using the year and day-of-year, effectively meaning that the month
and day-of-month are ignored during the resolving phase.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

In a similar manner, this method can be used to ignore secondary fields that
would otherwise be cross-checked. For example, if the formatter consists of year,
month, day-of-month and day-of-week, then there is only one way to resolve a
date, but the parsed value for day-of-week will be cross-checked against the
resolved date. Calling this method with the arguments

YEAR

,

MONTH_OF_YEAR

and

DAY_OF_MONTH

will ensure that the date is
resolved correctly, but without any cross-check for the day-of-week.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

In implementation terms, this method behaves as follows. The result of the
parsing phase can be considered to be a map of field to value. The behavior
of this method is to cause that map to be filtered between phase 1 and 2,
removing all fields other than those specified as arguments to this method.

This instance is immutable and unaffected by this method call.

This instance is immutable and unaffected by this method call.

format

```java
public
String
format​(
TemporalAccessor
temporal)
```

Formats a date-time object using this formatter.

This formats the date-time to a String using the rules of the formatter.

**Parameters:** temporal

- the temporal object to format, not null
**Returns:** the formatted string, not null
**Throws:** DateTimeException

- if an error occurs during formatting

---

#### format

public

String

format​(

TemporalAccessor

temporal)

Formats a date-time object using this formatter.

This formats the date-time to a String using the rules of the formatter.

This formats the date-time to a String using the rules of the formatter.

formatTo

```java
public void formatTo​(
TemporalAccessor
temporal,

Appendable
appendable)
```

Formats a date-time object to an

Appendable

using this formatter.

This outputs the formatted date-time to the specified destination.

Appendable

is a general purpose interface that is implemented by all
key character output classes including

StringBuffer

,

StringBuilder

,

PrintStream

and

Writer

.

Although

Appendable

methods throw an

IOException

, this method does not.
Instead, any

IOException

is wrapped in a runtime exception.

**Parameters:** temporal

- the temporal object to format, not null
**Parameters:** appendable

- the appendable to format to, not null
**Throws:** DateTimeException

- if an error occurs during formatting

---

#### formatTo

public void formatTo​(

TemporalAccessor

temporal,

Appendable

appendable)

Formats a date-time object to an

Appendable

using this formatter.

This outputs the formatted date-time to the specified destination.

Appendable

is a general purpose interface that is implemented by all
key character output classes including

StringBuffer

,

StringBuilder

,

PrintStream

and

Writer

.

Although

Appendable

methods throw an

IOException

, this method does not.
Instead, any

IOException

is wrapped in a runtime exception.

This outputs the formatted date-time to the specified destination.

Appendable

is a general purpose interface that is implemented by all
key character output classes including

StringBuffer

,

StringBuilder

,

PrintStream

and

Writer

.

Although

Appendable

methods throw an

IOException

, this method does not.
Instead, any

IOException

is wrapped in a runtime exception.

Although

Appendable

methods throw an

IOException

, this method does not.
Instead, any

IOException

is wrapped in a runtime exception.

parse

```java
public
TemporalAccessor
parse​(
CharSequence
text)
```

Fully parses the text producing a temporal object.

This parses the entire text producing a temporal object.
It is typically more useful to use

parse(CharSequence, TemporalQuery)

.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Parameters:** text

- the text to parse, not null
**Returns:** the parsed temporal object, not null
**Throws:** DateTimeParseException

- if unable to parse the requested result

---

#### parse

public

TemporalAccessor

parse​(

CharSequence

text)

Fully parses the text producing a temporal object.

This parses the entire text producing a temporal object.
It is typically more useful to use

parse(CharSequence, TemporalQuery)

.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

This parses the entire text producing a temporal object.
It is typically more useful to use

parse(CharSequence, TemporalQuery)

.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

parse

```java
public
TemporalAccessor
parse​(
CharSequence
text,

ParsePosition
position)
```

Parses the text using this formatter, providing control over the text position.

This parses the text without requiring the parse to start from the beginning
of the string or finish at the end.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

The operation of this method is slightly different to similar methods using

ParsePosition

on

java.text.Format

. That class will return
errors using the error index on the

ParsePosition

. By contrast, this
method will throw a

DateTimeParseException

if an error occurs, with
the exception containing the error index.
This change in behavior is necessary due to the increased complexity of
parsing and resolving dates/times in this API.

If the formatter parses the same field more than once with different values,
the result will be an error.

**Parameters:** text

- the text to parse, not null
**Parameters:** position

- the position to parse from, updated with length parsed
and the index of any error, not null
**Returns:** the parsed temporal object, not null
**Throws:** DateTimeParseException

- if unable to parse the requested result
**Throws:** IndexOutOfBoundsException

- if the position is invalid

---

#### parse

public

TemporalAccessor

parse​(

CharSequence

text,

ParsePosition

position)

Parses the text using this formatter, providing control over the text position.

This parses the text without requiring the parse to start from the beginning
of the string or finish at the end.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

The operation of this method is slightly different to similar methods using

ParsePosition

on

java.text.Format

. That class will return
errors using the error index on the

ParsePosition

. By contrast, this
method will throw a

DateTimeParseException

if an error occurs, with
the exception containing the error index.
This change in behavior is necessary due to the increased complexity of
parsing and resolving dates/times in this API.

If the formatter parses the same field more than once with different values,
the result will be an error.

This parses the text without requiring the parse to start from the beginning
of the string or finish at the end.
The result of this method is

TemporalAccessor

which has been resolved,
applying basic validation checks to help ensure a valid date-time.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

The operation of this method is slightly different to similar methods using

ParsePosition

on

java.text.Format

. That class will return
errors using the error index on the

ParsePosition

. By contrast, this
method will throw a

DateTimeParseException

if an error occurs, with
the exception containing the error index.
This change in behavior is necessary due to the increased complexity of
parsing and resolving dates/times in this API.

If the formatter parses the same field more than once with different values,
the result will be an error.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

The operation of this method is slightly different to similar methods using

ParsePosition

on

java.text.Format

. That class will return
errors using the error index on the

ParsePosition

. By contrast, this
method will throw a

DateTimeParseException

if an error occurs, with
the exception containing the error index.
This change in behavior is necessary due to the increased complexity of
parsing and resolving dates/times in this API.

If the formatter parses the same field more than once with different values,
the result will be an error.

The operation of this method is slightly different to similar methods using

ParsePosition

on

java.text.Format

. That class will return
errors using the error index on the

ParsePosition

. By contrast, this
method will throw a

DateTimeParseException

if an error occurs, with
the exception containing the error index.
This change in behavior is necessary due to the increased complexity of
parsing and resolving dates/times in this API.

If the formatter parses the same field more than once with different values,
the result will be an error.

If the formatter parses the same field more than once with different values,
the result will be an error.

parse

```java
public <T> T parse​(
CharSequence
text,

TemporalQuery
<T> query)
```

Fully parses the text producing an object of the specified type.

Most applications should use this method for parsing.
It parses the entire text to produce the required date-time.
The query is typically a method reference to a

from(TemporalAccessor)

method.
For example:

```java
LocalDateTime dt = parser.parse(str, LocalDateTime::from);
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Type Parameters:** T

- the type of the parsed date-time
**Parameters:** text

- the text to parse, not null
**Parameters:** query

- the query defining the type to parse to, not null
**Returns:** the parsed date-time, not null
**Throws:** DateTimeParseException

- if unable to parse the requested result

---

#### parse

public <T> T parse​(

CharSequence

text,

TemporalQuery

<T> query)

Fully parses the text producing an object of the specified type.

Most applications should use this method for parsing.
It parses the entire text to produce the required date-time.
The query is typically a method reference to a

from(TemporalAccessor)

method.
For example:

```java
LocalDateTime dt = parser.parse(str, LocalDateTime::from);
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

Most applications should use this method for parsing.
It parses the entire text to produce the required date-time.
The query is typically a method reference to a

from(TemporalAccessor)

method.
For example:

```java
LocalDateTime dt = parser.parse(str, LocalDateTime::from);
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

LocalDateTime dt = parser.parse(str, LocalDateTime::from);

parseBest

```java
public
TemporalAccessor
parseBest​(
CharSequence
text,

TemporalQuery
<?>... queries)
```

Fully parses the text producing an object of one of the specified types.

This parse method is convenient for use when the parser can handle optional elements.
For example, a pattern of 'uuuu-MM-dd HH.mm[ VV]' can be fully parsed to a

ZonedDateTime

,
or partially parsed to a

LocalDateTime

.
The queries must be specified in order, starting from the best matching full-parse option
and ending with the worst matching minimal parse option.
The query is typically a method reference to a

from(TemporalAccessor)

method.

The result is associated with the first type that successfully parses.
Normally, applications will use

instanceof

to check the result.
For example:

```java
TemporalAccessor dt = parser.parseBest(str, ZonedDateTime::from, LocalDateTime::from);
if (dt instanceof ZonedDateTime) {
...
} else {
...
}
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

**Parameters:** text

- the text to parse, not null
**Parameters:** queries

- the queries defining the types to attempt to parse to,
must implement

TemporalAccessor

, not null
**Returns:** the parsed date-time, not null
**Throws:** IllegalArgumentException

- if less than 2 types are specified
**Throws:** DateTimeParseException

- if unable to parse the requested result

---

#### parseBest

public

TemporalAccessor

parseBest​(

CharSequence

text,

TemporalQuery

<?>... queries)

Fully parses the text producing an object of one of the specified types.

This parse method is convenient for use when the parser can handle optional elements.
For example, a pattern of 'uuuu-MM-dd HH.mm[ VV]' can be fully parsed to a

ZonedDateTime

,
or partially parsed to a

LocalDateTime

.
The queries must be specified in order, starting from the best matching full-parse option
and ending with the worst matching minimal parse option.
The query is typically a method reference to a

from(TemporalAccessor)

method.

The result is associated with the first type that successfully parses.
Normally, applications will use

instanceof

to check the result.
For example:

```java
TemporalAccessor dt = parser.parseBest(str, ZonedDateTime::from, LocalDateTime::from);
if (dt instanceof ZonedDateTime) {
...
} else {
...
}
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

This parse method is convenient for use when the parser can handle optional elements.
For example, a pattern of 'uuuu-MM-dd HH.mm[ VV]' can be fully parsed to a

ZonedDateTime

,
or partially parsed to a

LocalDateTime

.
The queries must be specified in order, starting from the best matching full-parse option
and ending with the worst matching minimal parse option.
The query is typically a method reference to a

from(TemporalAccessor)

method.

The result is associated with the first type that successfully parses.
Normally, applications will use

instanceof

to check the result.
For example:

```java
TemporalAccessor dt = parser.parseBest(str, ZonedDateTime::from, LocalDateTime::from);
if (dt instanceof ZonedDateTime) {
...
} else {
...
}
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

The result is associated with the first type that successfully parses.
Normally, applications will use

instanceof

to check the result.
For example:

```java
TemporalAccessor dt = parser.parseBest(str, ZonedDateTime::from, LocalDateTime::from);
if (dt instanceof ZonedDateTime) {
...
} else {
...
}
```

If the parse completes without reading the entire length of the text,
or a problem occurs during parsing or merging, then an exception is thrown.

TemporalAccessor dt = parser.parseBest(str, ZonedDateTime::from, LocalDateTime::from);
if (dt instanceof ZonedDateTime) {
...
} else {
...
}

parseUnresolved

```java
public
TemporalAccessor
parseUnresolved​(
CharSequence
text,

ParsePosition
position)
```

Parses the text using this formatter, without resolving the result, intended
for advanced use cases.

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.
This method performs the parsing stage but not the resolving stage.

The result of this method is

TemporalAccessor

which represents the
data as seen in the input. Values are not validated, thus parsing a date string
of '2012-00-65' would result in a temporal with three fields - year of '2012',
month of '0' and day-of-month of '65'.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

Errors are returned using the error index field of the

ParsePosition

instead of

DateTimeParseException

.
The returned error index will be set to an index indicative of the error.
Callers must check for errors before using the result.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

**Parameters:** text

- the text to parse, not null
**Parameters:** position

- the position to parse from, updated with length parsed
and the index of any error, not null
**Returns:** the parsed text, null if the parse results in an error
**Throws:** DateTimeException

- if some problem occurs during parsing
**Throws:** IndexOutOfBoundsException

- if the position is invalid

---

#### parseUnresolved

public

TemporalAccessor

parseUnresolved​(

CharSequence

text,

ParsePosition

position)

Parses the text using this formatter, without resolving the result, intended
for advanced use cases.

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.
This method performs the parsing stage but not the resolving stage.

The result of this method is

TemporalAccessor

which represents the
data as seen in the input. Values are not validated, thus parsing a date string
of '2012-00-65' would result in a temporal with three fields - year of '2012',
month of '0' and day-of-month of '65'.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

Errors are returned using the error index field of the

ParsePosition

instead of

DateTimeParseException

.
The returned error index will be set to an index indicative of the error.
Callers must check for errors before using the result.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

Parsing is implemented as a two-phase operation.
First, the text is parsed using the layout defined by the formatter, producing
a

Map

of field to value, a

ZoneId

and a

Chronology

.
Second, the parsed data is

resolved

, by validating, combining and
simplifying the various fields into more useful ones.
This method performs the parsing stage but not the resolving stage.

The result of this method is

TemporalAccessor

which represents the
data as seen in the input. Values are not validated, thus parsing a date string
of '2012-00-65' would result in a temporal with three fields - year of '2012',
month of '0' and day-of-month of '65'.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

Errors are returned using the error index field of the

ParsePosition

instead of

DateTimeParseException

.
The returned error index will be set to an index indicative of the error.
Callers must check for errors before using the result.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

The result of this method is

TemporalAccessor

which represents the
data as seen in the input. Values are not validated, thus parsing a date string
of '2012-00-65' would result in a temporal with three fields - year of '2012',
month of '0' and day-of-month of '65'.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

Errors are returned using the error index field of the

ParsePosition

instead of

DateTimeParseException

.
The returned error index will be set to an index indicative of the error.
Callers must check for errors before using the result.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

The text will be parsed from the specified start

ParsePosition

.
The entire length of the text does not have to be parsed, the

ParsePosition

will be updated with the index at the end of parsing.

Errors are returned using the error index field of the

ParsePosition

instead of

DateTimeParseException

.
The returned error index will be set to an index indicative of the error.
Callers must check for errors before using the result.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

Errors are returned using the error index field of the

ParsePosition

instead of

DateTimeParseException

.
The returned error index will be set to an index indicative of the error.
Callers must check for errors before using the result.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

If the formatter parses the same field more than once with different values,
the result will be an error.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

This method is intended for advanced use cases that need access to the
internal state during parsing. Typical application code should use

parse(CharSequence, TemporalQuery)

or the parse method on the target type.

toFormat

```java
public
Format
toFormat()
```

Returns this formatter as a

java.text.Format

instance.

The returned

Format

instance will format any

TemporalAccessor

and parses to a resolved

TemporalAccessor

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

**Returns:** this formatter as a classic format instance, not null

---

#### toFormat

public

Format

toFormat()

Returns this formatter as a

java.text.Format

instance.

The returned

Format

instance will format any

TemporalAccessor

and parses to a resolved

TemporalAccessor

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

The returned

Format

instance will format any

TemporalAccessor

and parses to a resolved

TemporalAccessor

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

toFormat

```java
public
Format
toFormat​(
TemporalQuery
<?> parseQuery)
```

Returns this formatter as a

java.text.Format

instance that will
parse using the specified query.

The returned

Format

instance will format any

TemporalAccessor

and parses to the type specified.
The type must be one that is supported by

parse(java.lang.CharSequence)

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

**Parameters:** parseQuery

- the query defining the type to parse to, not null
**Returns:** this formatter as a classic format instance, not null

---

#### toFormat

public

Format

toFormat​(

TemporalQuery

<?> parseQuery)

Returns this formatter as a

java.text.Format

instance that will
parse using the specified query.

The returned

Format

instance will format any

TemporalAccessor

and parses to the type specified.
The type must be one that is supported by

parse(java.lang.CharSequence)

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

The returned

Format

instance will format any

TemporalAccessor

and parses to the type specified.
The type must be one that is supported by

parse(java.lang.CharSequence)

.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

Exceptions will follow the definitions of

Format

, see those methods
for details about

IllegalArgumentException

during formatting and

ParseException

or null during parsing.
The format does not support attributing of the returned format string.

toString

```java
public
String
toString()
```

Returns a description of the underlying formatters.

**Overrides:** toString

in class

Object
**Returns:** a description of this formatter, not null

---

#### toString

public

String

toString()

Returns a description of the underlying formatters.

---

