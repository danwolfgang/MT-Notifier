#!/usr/bin/perl -w

# =======================================================================
# Copyright 2003-2005, Everitz Consulting (mt@everitz.com)
#
# Non-commercial entities and non-profit organizations are granted a no-
# charge license to use the software however they like, and modify it to
# their needs, but redistribution of the software is not allowed under
# any circumstances. No support is included with this no-charge license.
# Contact us if you would like to purchase support for any product so
# licensed.
#
# Under no circumstances and under no legal theory, whether in tort
# (including negligence), contract, or otherwise, shall Everitz
# Consulting be liable to any person for any direct, indirect, special,
# incidental, or consequential damages of any character arising as a
# result of this License or the use of the Original Work including,
# without limitation, damages for loss of goodwill, work stoppage,
# computer failure or malfunction, or any and all other commercial
# damages or losses.
#
# Not to be redistributed without permssion of the copyright holder.
# =======================================================================

use strict;

my($MT_DIR);
BEGIN {
  if ($0 =~ m!(.*[/\\])!) {
    $MT_DIR = $1;
  } else {
    $MT_DIR = './';
  }
  unshift @INC, $MT_DIR . 'lib';
  unshift @INC, $MT_DIR . 'extlib';
}

eval {
  require Everitz::Notifier;
  my $app = Everitz::Notifier->new (
    Config => $MT_DIR . 'mt.cfg',
    Directory => $MT_DIR
  ) or die Everitz::Notifier->errstr;
  local $SIG{__WARN__} = sub { $app->trace ($_[0]) };
  $app->run;
};

if ($@) {
  print "Content-Type: text/html\n\n";
  print "An error occurred: $@";
}
