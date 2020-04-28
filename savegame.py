import sys
import struct

import tkinter as tk
from tkinter import ttk

soFromBeginning = 0
soFromCurrent = 1

class Boolean:
    Size = 1

    @staticmethod
    def Convert(bytes):
        return int.from_bytes(bytes, byteorder='little') != 0

class Byte:
    Size = 1

    @staticmethod
    def Convert(bytes):
        return int.from_bytes(bytes, byteorder='little', signed=False)

class Word:
    Size = 2

    @staticmethod
    def Convert(bytes):
        return int.from_bytes(bytes, byteorder='little', signed=False)

class ShortInt:
    Size = 1

    @staticmethod
    def Convert(bytes):
        return int.from_bytes(bytes, byteorder='little')

class LongInt:
    Size = 4

    @staticmethod
    def Convert(bytes):
        return int.from_bytes(bytes, byteorder='little')

class Double:
    Size = 8

    @staticmethod
    def Convert(bytes):
        return struct.unpack('d', bytes)[0]

class String:
    @staticmethod
    def Convert(bytes):
        return bytes.decode("latin-1").rstrip('\0')

class Char:
    Size = 1

    @staticmethod
    def Convert(bytes):
        return String.Convert(bytes)[0]

class ShortText:
    Size = 26*Char.Size

    @staticmethod
    def Convert(bytes):
        return String.Convert(bytes)

class StandardText:
    Size = 51*Char.Size

    @staticmethod
    def Convert(bytes):
        return String.Convert(bytes)

class CMDate:
    Size = Word.Size + Word.Size + LongInt.Size

    @staticmethod
    def Convert(bytes):
        date = CMDate()

        position = 0

        date.Day = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        date.Year = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        date.LeapYear = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        return date

class PNation:
    Size = LongInt.Size

class PDivision:
    Size = LongInt.Size

class PClub:
    Size = LongInt.Size

class PName:
    Size = LongInt.Size

class PPlayer:
    Size = LongInt.Size

class PNonPlayer:
    Size = LongInt.Size

class PStaff:
    Size = LongInt.Size

class PContract:
    Size = LongInt.Size


class Block:
    Size = 268

    @staticmethod
    def Load(bytes):
        block = Block()

        position = 0

        block.Position = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        block.Size = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        block.Name = String.Convert(bytes[position:position+260*Char.Size])
        position += 260*Char.Size

        return block


class Nation:
    Size = 290

    @staticmethod
    def Load(bytes):
        nation = Nation()

        position = 0

        nation.ID = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.Name = StandardText.Convert(bytes[position:position+StandardText.Size])
        position += StandardText.Size

        nation.GenderName = Char.Convert(bytes[position:position+Char.Size])
        position += Char.Size

        nation.ShortName = ShortText.Convert(bytes[position:position+ShortText.Size])
        position += ShortText.Size

        nation.GenderShortName = Char.Convert(bytes[position:position+Char.Size])
        position += Char.Size

        nation.ThreeLetterName = String.Convert(bytes[position:position+4*Char.Size])
        position += 4*Char.Size

        nation.Nationality = ShortText.Convert(bytes[position:position+ShortText.Size])
        position += ShortText.Size

        nation.Continent = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.Region = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.ActualRegion = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.FirstLanguage = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.SecondLanguage = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.ThirdLanguage = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.Capital = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.StateOfDevelopment = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.GroupMembership = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.NationalStadium = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.GameImportance = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.LeagueStandard = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.NumberClubs = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        nation.NumberStaff = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.UpdateDay = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        nation.Reputation = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        nation.ForeColour1 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.BackColour1 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.ForeColour2 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.BackColour2 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.ForeColour3 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.BackColour3 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.FIFACoefficient = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.FIFACoefficient91 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.FIFACoefficient92 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.FIFACoefficient93 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.FIFACoefficient94 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.FIFACoefficient95 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.FIFACoefficient96 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.UEFACoefficient91 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.UEFACoefficient92 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.UEFACoefficient93 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.UEFACoefficient94 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.UEFACoefficient95 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.UEFACoefficient96 = Double.Convert(bytes[position:position+Double.Size])
        position += Double.Size

        nation.Rival1 = bytes[position:position+PNation.Size]
        position += PNation.Size

        nation.Rival2 = bytes[position:position+PNation.Size]
        position += PNation.Size

        nation.Rival3 = bytes[position:position+PNation.Size]
        position += PNation.Size

        nation.LeagueSelected = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nation.ShortlistOffset = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nation.GamesPlayed = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        return nation


class Division:
    Size = 107

    @staticmethod
    def Load(bytes):
        division = Division()

        position = 0

        division.ID = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        division.Name = StandardText.Convert(bytes[position:position+StandardText.Size])
        position += StandardText.Size

        division.GenderName = Char.Convert(bytes[position:position+Char.Size])
        position += Char.Size

        division.ShortName = ShortText.Convert(bytes[position:position+ShortText.Size])
        position += ShortText.Size

        division.GenderShortName = Char.Convert(bytes[position:position+Char.Size])
        position += Char.Size

        division.ThreeLetterName = String.Convert(bytes[position:position+4*Char.Size])
        position += 4*Char.Size

        division.Scope = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        division.Selected = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        division.Continent = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        division.Nation = bytes[position:position+PNation.Size]
        position += PNation.Size

        division.ForeColour = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        division.BackColour = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        division.Reputation = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        return division


class Club:
    Size = 581

    @staticmethod
    def Load(bytes):
        club = Club()

        position = 0

        club.ID = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.Name = StandardText.Convert(bytes[position:position+StandardText.Size])
        position += StandardText.Size

        club.GenderName = Char.Convert(bytes[position:position+Char.Size])
        position += Char.Size

        club.ShortName = ShortText.Convert(bytes[position:position+ShortText.Size])
        position += ShortText.Size

        club.ShortGenderName = Char.Convert(bytes[position:position+Char.Size])
        position += Char.Size

        club.Nation = bytes[position:position+PNation.Size]
        position += PNation.Size

        club.Division = bytes[position:position+PDivision.Size]
        position += PDivision.Size

        club.LastDivision = bytes[position:position+PDivision.Size]
        position += PDivision.Size

        club.LastPosition = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        club.ReserveDivision = bytes[position:position+PDivision.Size]
        position += PDivision.Size

        club.ProfessionalStatus = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        club.Cash = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.Stadium = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.OwnStatus = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        club.ReserveStadium = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.MatchDay = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        club.Attendance = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.MinAttendance = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.MaxAttendance = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.Training = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        club.Reputation = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        club.PLC = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        club.ForeColour1 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.BackColour1 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.ForeColour2 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.BackColour2 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.ForeColour3 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.BackColour3 = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.FavStaff1 = bytes[position:position+PStaff.Size]
        position += PStaff.Size

        club.FavStaff2 = bytes[position:position+PStaff.Size]
        position += PStaff.Size

        club.FavStaff3 = bytes[position:position+PStaff.Size]
        position += PStaff.Size

        club.DisStaff1 = bytes[position:position+PStaff.Size]
        position += PStaff.Size

        club.DisStaff2 = bytes[position:position+PStaff.Size]
        position += PStaff.Size

        club.DisStaff3 = bytes[position:position+PStaff.Size]
        position += PStaff.Size

        club.Rival1 = bytes[position:position+PClub.Size]
        position += PClub.Size

        club.Rival2 = bytes[position:position+PClub.Size]
        position += PClub.Size

        club.Rival3 = bytes[position:position+PClub.Size]
        position += PClub.Size

        club.Chairman = bytes[position:position+PStaff.Size]
        position += PStaff.Size

        club.Directors = []
        for j in range(3):
            club.Directors.append(bytes[position:position+PStaff.Size])
            position += PStaff.Size

        club.Manager = bytes[position:position+PStaff.Size]
        position += PStaff.Size

        club.AssistantManager = bytes[position:position+PStaff.Size]
        position += PStaff.Size

        club.Squad = []
        for j in range(50):
            club.Squad.append(bytes[position:position+PStaff.Size])
            position += PStaff.Size

        club.Coaches = []
        for j in range(5):
            club.Coaches.append(bytes[position:position+PStaff.Size])
            position += PStaff.Size

        club.Scouts = []
        for j in range(7):
            club.Scouts.append(bytes[position:position+PStaff.Size])
            position += PStaff.Size

        club.Physios = []
        for j in range(3):
            club.Physios.append(bytes[position:position+PStaff.Size])
            position += PStaff.Size

        club.EuroFlag = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.EuroSeeding = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        club.TeamSelected = []
        for j in range(20):
            club.TeamSelected.append(bytes[position:position+PStaff.Size])
            position += PStaff.Size

        club.TacticTraining = []
        for j in range(20):
            club.TacticTraining.append(LongInt.Convert(bytes[position:position+LongInt.Size]))
            position += LongInt.Size

        club.TacticSelected = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        club.HasLinkedClub = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        return club


class Name:
    Size = 60

    @staticmethod
    def Load(bytes):
        name = Name()

        position = 0

        name.Name = StandardText.Convert(bytes[position:position+StandardText.Size])
        position += StandardText.Size

        name.ID = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        name.Nation = bytes[position:position+PNation.Size]
        position += PNation.Size

        name.Count = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        return name


class Player:
    Size = 70

    @staticmethod
    def Load(bytes):
        player = Player()

        position = 0

        player.ID = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        player.SquadNumber = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        player.CurrentAbility = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        player.PotentialAbility = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        player.HomeReputation = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        player.CurrentReputation = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        player.WorldReputation = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        player.Sweeper = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Defender = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.DefensiveMidfielder = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Midfielder = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.AttackingMidfielder = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Attacker = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.WingBack = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.RightSide = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.LeftSide = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Central = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.FreeRole = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Acceleration = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Aggression = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Agility = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Anticipation = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Balance = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Bravery = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Consistency = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Corners = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Crossing = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Decisions = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Dirtiness = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Dribbling = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Finishing = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Flair = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.FreeKicks = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Handling = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Heading = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.ImportantMatches = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.InjuryProneness = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Jumping = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Leadership = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.LeftFoot = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.LongShots = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Marking = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Movement = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.NaturalFitness = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.OneOnOnes = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.PlayerPace = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Passing = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Penalties = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Positioning = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Reflexes = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.RightFoot = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Stamina = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Strength = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Tackling = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Teamwork = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Technique = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.ThrowIns = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Versatility = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.Vision = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.WorkRate = ShortInt.Convert(bytes[position:position+ShortInt.Size])
        position += ShortInt.Size

        player.PlayerMorale = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        player.Scouted = Boolean.Convert(bytes[position:position+Boolean.Size])
        position += Boolean.Size

        # player.GKScout = Double.Convert(bytes[position:position+Double.Size])
        # position += Double.Size
        #
        # player.DScout = Double.Convert(bytes[position:position+Double.Size])
        # position += Double.Size
        #
        # player.DMScout = Double.Convert(bytes[position:position+Double.Size])
        # position += Double.Size
        #
        # player.MScout = Double.Convert(bytes[position:position+Double.Size])
        # position += Double.Size
        #
        # player.AMScout = Double.Convert(bytes[position:position+Double.Size])
        # position += Double.Size
        #
        # player.WScout = Double.Convert(bytes[position:position+Double.Size])
        # position += Double.Size
        #
        # player.AScout = Double.Convert(bytes[position:position+Double.Size])
        # position += Double.Size

        return player


class NonPlayer:
    Size = 68

    @staticmethod
    def Load(bytes):
        nonplayer = NonPlayer()

        position = 0

        nonplayer.ID = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nonplayer.CurrentAbility = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        nonplayer.PotentialAbility = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        nonplayer.HomeReputation = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        nonplayer.CurrentReputation = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        nonplayer.WorldReputation = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        nonplayer.Attacking = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Business = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Coaching = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.CoachingGks = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.CoachingTechnique = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Directness = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Discipline = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.FreeRoles = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Interference = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Judgement = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.JudgingPotential = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.ManHandling = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Marking = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Motivating = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Offside = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Patience = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Physiotherapy = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Pressing = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Resources = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Tactics = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Youngsters = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        nonplayer.Goalkeeper = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nonplayer.Sweeper = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nonplayer.Defender = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nonplayer.DefensiveMidfielder = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nonplayer.Midfielder = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nonplayer.AttackingMidfielder = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nonplayer.Attacker = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nonplayer.WingBack = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        nonplayer.Formation = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        return nonplayer


class Staff:
    Size = 110

    @staticmethod
    def Load(bytes):
        staff = Staff()

        position = 0

        staff.ID = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        staff.FirstName = bytes[position:position+PName.Size]
        position += PName.Size

        staff.SecondName = bytes[position:position+PName.Size]
        position += PName.Size

        staff.CommonName = bytes[position:position+PName.Size]
        position += PName.Size

        staff.DateOfBirth = CMDate.Convert(bytes[position:position+CMDate.Size])
        position += CMDate.Size

        staff.YearOfBirth = Word.Convert(bytes[position:position+Word.Size])
        position += Word.Size

        staff.Nation = bytes[position:position+PNation.Size]
        position += PNation.Size

        staff.SecondNation = bytes[position:position+PNation.Size]
        position += PNation.Size

        staff.IntApps = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.IntGoals = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.NationalJob = bytes[position:position+PNation.Size]
        position += PNation.Size

        staff.JobForNation = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.DateJoinedNation = CMDate.Convert(bytes[position:position+CMDate.Size])
        position += CMDate.Size

        staff.DateExpiresNation = CMDate.Convert(bytes[position:position+CMDate.Size])
        position += CMDate.Size

        staff.ClubJob = bytes[position:position+PClub.Size]
        position += PClub.Size

        staff.JobForClub = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.DateJoinedClub = CMDate.Convert(bytes[position:position+CMDate.Size])
        position += CMDate.Size

        staff.DateExpiresClub = CMDate.Convert(bytes[position:position+CMDate.Size])
        position += CMDate.Size

        staff.Wage = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        staff.Value = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        staff.Adaptability = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Ambition = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Determination = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Loyality = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Pressure = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Professionalism = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Sportsmanship = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Temperament = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.PlayingSquad = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Classification = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.ClubValuation = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Player = bytes[position:position+PPlayer.Size]
        position += PPlayer.Size

        staff.StaffPreferences = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        staff.NonPlayer = bytes[position:position+PNonPlayer.Size]
        position += PNonPlayer.Size

        staff.SquadSelectedFor = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        staff.Contract = bytes[position:position+PContract.Size]
        position += PContract.Size

        staff.LoanContract = bytes[position:position+PContract.Size]
        position += PContract.Size

        return staff

    def entry(this):
        result = []
        # result.append("{} {}".format(this.FirstName.Name, this.SecondName.Name))
        result.append("{}".format(this.CommonName.Name))
        result.append(this.Nation.Name)
        result.append(this.ClubJob.Name)
        # result.append(this.Player.?) # Position
        result.append(this.Player.CurrentAbility)
        result.append(this.Player.PotentialAbility)
        # result.append(this.Player.?) # Age
        result.append("{:,}".format(this.Value))
        # result.append(this.Player.?)
        return result


class Contract:
    Size = 80

    @staticmethod
    def Load(bytes):
        contract = Contract()

        position = 0

        contract.ID = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        contract.Club = bytes[position:position+PClub.Size]
        position += PClub.Size

        contract.Unknown1 = []
        for j in range(4):
            contract.Unknown1.append(Byte.Convert(bytes[position:position+Byte.Size]))
            position += Byte.Size

        contract.Wage = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        contract.GoalBonus = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        contract.AssistBonus = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        contract.CleanSheetBonus = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        contract.NonPromotionRC = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        contract.MinimumFeeRC = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        contract.NonPlayingRC = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        contract.RelegationRC = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        contract.ManagerJobRC = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        contract.ReleaseFee = LongInt.Convert(bytes[position:position+LongInt.Size])
        position += LongInt.Size

        contract.DateStarted = CMDate.Convert(bytes[position:position+CMDate.Size])
        position += CMDate.Size

        contract.ContractExpires = CMDate.Convert(bytes[position:position+CMDate.Size])
        position += CMDate.Size

        contract.ContractType = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        contract.Unknown2 = []
        for j in range(19):
            contract.Unknown2.append(Byte.Convert(bytes[position:position+Byte.Size]))
            position += Byte.Size

        contract.LeavingOnBosman = Boolean.Convert(bytes[position:position+Boolean.Size])
        position += Boolean.Size

        contract.TransferArrangedFor = bytes[position:position+PClub.Size]
        position += PClub.Size

        contract.TransferStatus = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        contract.SquadStatus = Byte.Convert(bytes[position:position+Byte.Size])
        position += Byte.Size

        return contract


def AssignPointer(ptr, Container):
    if int.from_bytes(ptr, byteorder='little') >= 0 and int.from_bytes(ptr, byteorder='little') < len(Container):
        return Container[int.from_bytes(ptr, byteorder='little')]
    else:
        return None


FlstNation = []

def LoadNations():
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'nation.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intCount = FlstBlock[j].Size // Nation.Size

    for j in range(intCount):
        nation = Nation.Load(FcfsFile.read(Nation.Size))
        FlstNation.append(nation)

    for j in range(intCount):
        FlstNation[j].Rival1 = AssignPointer(FlstNation[j].Rival1, FlstNation)
        FlstNation[j].Rival2 = AssignPointer(FlstNation[j].Rival2, FlstNation)
        FlstNation[j].Rival3 = AssignPointer(FlstNation[j].Rival3, FlstNation)

FlstDivision = []

def LoadDivisions():
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'club_comp.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intCount = FlstBlock[j].Size // Division.Size

    for j in range(intCount):
        division = Division.Load(FcfsFile.read(Division.Size))
        FlstDivision.append(division)
        FlstDivision[j].Nation = AssignPointer(FlstDivision[j].Nation, FlstNation)


FlstClub = []

def LoadClubs():
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'club.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intCount = FlstBlock[j].Size // Club.Size

    for j in range(intCount):
        club = Club.Load(FcfsFile.read(Club.Size))
        FlstClub.append(club)
        FlstClub[j].Nation = AssignPointer(FlstClub[j].Nation, FlstNation)
        FlstClub[j].Division = AssignPointer(FlstClub[j].Division, FlstDivision)
        FlstClub[j].LastDivision = AssignPointer(FlstClub[j].LastDivision, FlstDivision)
        FlstClub[j].ReserveDivision = AssignPointer(FlstClub[j].ReserveDivision, FlstDivision)

    for j in range(intCount):
        FlstClub[j].Rival1 = AssignPointer(FlstClub[j].Rival1, FlstClub)
        FlstClub[j].Rival2 = AssignPointer(FlstClub[j].Rival2, FlstClub)
        FlstClub[j].Rival3 = AssignPointer(FlstClub[j].Rival3, FlstClub)


FlstFirstName = []
FlstSecondName = []
FlstCommonName = []

def LoadNames():
    # First Names
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'first_names.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intCount = FlstBlock[j].Size // Name.Size

    for j in range(intCount):
        name = Name.Load(FcfsFile.read(Name.Size))
        FlstFirstName.append(name)
        FlstFirstName[j].Nation = AssignPointer(FlstFirstName[j].Nation, FlstNation)

    # Second Names
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'second_names.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intCount = FlstBlock[j].Size // Name.Size

    for j in range(intCount):
        name = Name.Load(FcfsFile.read(Name.Size))
        FlstSecondName.append(name)
        FlstSecondName[j].Nation = AssignPointer(FlstSecondName[j].Nation, FlstNation)

    # Common Names
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'common_names.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intCount = FlstBlock[j].Size // Name.Size

    for j in range(intCount):
        name = Name.Load(FcfsFile.read(Name.Size))
        FlstCommonName.append(name)
        FlstCommonName[j].Nation = AssignPointer(FlstCommonName[j].Nation, FlstNation)


FlstPlayer = []

def LoadPlayers():
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'player.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intCount = FlstBlock[j].Size // Player.Size

    for j in range(intCount):
        player = Player.Load(FcfsFile.read(Player.Size))
        FlstPlayer.append(player)
        # PlayerConvert()


FlstNonPlayer = []

def LoadNonPlayers():
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'nonplayer.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intCount = FlstBlock[j].Size // NonPlayer.Size

    for j in range(intCount):
        nonplayer = NonPlayer.Load(FcfsFile.read(NonPlayer.Size))
        FlstNonPlayer.append(nonplayer)


FlstStaff = []

def LoadStaffs():
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'staff.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intCount = FlstBlock[j].Size // Staff.Size

    for j in range(intCount):
        staff = Staff.Load(FcfsFile.read(Staff.Size))
        staff.Contract = None
        staff.LoanContract = None
        FlstStaff.append(staff)
        FlstStaff[j].FirstName = AssignPointer(FlstStaff[j].FirstName, FlstFirstName)
        FlstStaff[j].SecondName = AssignPointer(FlstStaff[j].SecondName, FlstSecondName)
        FlstStaff[j].CommonName = AssignPointer(FlstStaff[j].CommonName, FlstCommonName)
        FlstStaff[j].Nation = AssignPointer(FlstStaff[j].Nation, FlstNation)
        FlstStaff[j].SecondNation = AssignPointer(FlstStaff[j].SecondNation, FlstNation)
        FlstStaff[j].NationalJob = AssignPointer(FlstStaff[j].NationalJob, FlstNation)
        FlstStaff[j].ClubJob = AssignPointer(FlstStaff[j].ClubJob, FlstClub)
        FlstStaff[j].Player = AssignPointer(FlstStaff[j].Player, FlstPlayer)
        FlstStaff[j].NonPlayer = AssignPointer(FlstStaff[j].NonPlayer, FlstNonPlayer)

    for j in range(len(FlstClub)):
        FlstClub[j].FavStaff1 = AssignPointer(FlstClub[j].FavStaff1, FlstStaff)
        FlstClub[j].FavStaff2 = AssignPointer(FlstClub[j].FavStaff2, FlstStaff)
        FlstClub[j].FavStaff3 = AssignPointer(FlstClub[j].FavStaff3, FlstStaff)
        FlstClub[j].DisStaff1 = AssignPointer(FlstClub[j].DisStaff1, FlstStaff)
        FlstClub[j].DisStaff2 = AssignPointer(FlstClub[j].DisStaff2, FlstStaff)
        FlstClub[j].DisStaff3 = AssignPointer(FlstClub[j].DisStaff3, FlstStaff)
        FlstClub[j].Chairman = AssignPointer(FlstClub[j].Chairman, FlstStaff)
        FlstClub[j].Manager = AssignPointer(FlstClub[j].Manager, FlstStaff)
        FlstClub[j].AssistantManager = AssignPointer(FlstClub[j].AssistantManager, FlstStaff)

        for s in range(3):
            FlstClub[j].Directors[s] = AssignPointer(FlstClub[j].Directors[s], FlstStaff)
        for s in range(50):
            FlstClub[j].Squad[s] = AssignPointer(FlstClub[j].Squad[s], FlstStaff)
        for s in range(5):
            FlstClub[j].Coaches[s] = AssignPointer(FlstClub[j].Coaches[s], FlstStaff)
        for s in range(7):
            FlstClub[j].Scouts[s] = AssignPointer(FlstClub[j].Scouts[s], FlstStaff)
        for s in range(3):
            FlstClub[j].Physios[s] = AssignPointer(FlstClub[j].Physios[s], FlstStaff)
        for s in range(20):
            FlstClub[j].TeamSelected[s] = AssignPointer(FlstClub[j].TeamSelected[s], FlstStaff)


FlstContract = []

def LoadContracts():
    j = 0
    while j < len(FlstBlock) and FlstBlock[j].Name != 'contract.dat':
        j += 1

    FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
    intPreCount = int.from_bytes(FcfsFile.read(4), byteorder='little')
    intCount = int.from_bytes(FcfsFile.read(4), byteorder='little')

    byPre = []
    for j in range(intPreCount):
        byPre = [int.from_bytes(byte, byteorder='little', signed=False) for byte in FcfsFile.read(21)]

    if intPreCount > 0:
        intCount = byPre[17]

    for j in range(intCount):
        contract = Contract.Load(FcfsFile.read(Contract.Size))
        FlstContract.append(contract)
        FlstContract[j].Club = AssignPointer(FlstContract[j].Club, FlstClub)
        FlstContract[j].TransferArrangedFor = AssignPointer(FlstContract[j].TransferArrangedFor, FlstClub)
        if FlstContract[j].ID >= 0 and FlstContract[j].ID < len(FlstStaff):
            if FlstStaff[FlstContract[j].ID].Contract == None:
                FlstStaff[FlstContract[j].ID].Contract = FlstContract[j]
            else:
                if FlstStaff[FlstContract[j].ID].Contract.Club == FlstStaff[FlstContract[j].ID].ClubJob:
                    FlstStaff[FlstContract[j].ID].LoanContract = FlstStaff[FlstContract[j].ID].Contract
                    FlstStaff[FlstContract[j].ID].Contract = FlstContract[j]
                else:
                    FlstStaff[FlstContract[j].ID].LoanContract = FlstStaff[FlstContract[j].ID].Contract

# ---

filLoad = open(sys.argv[1], 'rb')

FboCompressed = int.from_bytes(filLoad.read(4), byteorder='little') == 4

filLoad.seek(4, soFromCurrent)
intTemp = int.from_bytes(filLoad.read(4), byteorder='little')

FlstBlock = []

for j in range(intTemp):
    newBlock = Block.Load(filLoad.read(Block.Size))
    FlstBlock.append(newBlock)

FcfsFile = open(sys.argv[1], 'rb') # uncompressed

j = 0
while j < len(FlstBlock) and FlstBlock[j].Name != 'general.dat':
    j += 1

FcfsFile.seek(FlstBlock[j].Position, soFromBeginning)
buffer = FcfsFile.read(3944)
FcmdGameData = CMDate.Convert(FcfsFile.read(CMDate.Size))

LoadNations()
LoadDivisions()
LoadClubs()
LoadNames()
LoadPlayers()
LoadNonPlayers()
LoadStaffs()
LoadContracts()

# ---

filScoutList = open(sys.argv[2], 'rb')

byPlsStart = filScoutList.read(6)

byPlsName = filScoutList.read(101).decode('latin-1')

byPlsManName = filScoutList.read(252).decode('latin-1')

byPlsMid = filScoutList.read(8)

count = int.from_bytes(filScoutList.read(4), byteorder='little')

FlcPlayers = []

for j in range(count):
    firstNameId = LongInt.Convert(filScoutList.read(4))
    secondNameId = LongInt.Convert(filScoutList.read(4))
    commonNameId = LongInt.Convert(filScoutList.read(4))
    id = LongInt.Convert(filScoutList.read(4))

    dateOfBirt = CMDate.Convert(filScoutList.read(CMDate.Size))

    FlcPlayers.append(id)

    byPlsZeros = filScoutList.read(20)
    byPlsDelimiter = filScoutList.read(1)

# ---

def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    if col in ["ability", "potability"]:
        l.sort(reverse=reverse, key=lambda val: int(val[0]))
    elif col in ["value"]:
        l.sort(reverse=reverse, key=lambda val: int(val[0].replace(",", "")))
    else:
        l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))


root = tk.Tk()
# root.geometry('800x600')
# frame = tk.Frame(root)
# frame.pack()
tree = ttk.Treeview(root, columns=["nation", "club", "ability", "potability", "value"])
tree.heading("#0", text="Name", command=lambda: treeview_sort_column(tree, "#0", False))
tree.heading("nation", text="Nation", command=lambda: treeview_sort_column(tree, "nation", False))
tree.heading("club", text="Club", command=lambda: treeview_sort_column(tree, "club", False))
tree.heading("ability", text="Ability", command=lambda: treeview_sort_column(tree, "ability", False))
tree.heading("potability", text="Pot Ability", command=lambda: treeview_sort_column(tree, "potability", False))
tree.heading("value", text="Value", command=lambda: treeview_sort_column(tree, "value", False))
for id in FlcPlayers:
    player = FlstStaff[id].entry()
    tree.insert('', 'end', text=player[0], values=player[1:])

tree.pack(expand=True, fill="both")
root.mainloop()
