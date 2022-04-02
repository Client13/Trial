import os
import discord
import pymongo
import aiohttp
import logging
import datetime
from discord.ext import commands, tasks

IGNORE = (
    927611170511290408,
    896278487491551262
    
)


class anti(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    async def ban(self, guild, user, *, reason: str = None):
        try:
            return await self.ban(guild, user, reason=reason)
        except Exception:
            return

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member,
                               after: discord.Member) -> None:
        await self.client.wait_until_ready()
        
        guild = after.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in after.guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.member_role_update):
            
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                if guild.me.guild_permissions.ban_members:
                    await guild.ban(entry.user,
                                   reason="R-Dynamic Protection System | Anti Member Role Update")
                for role in after.roles:
                  if role not in before.roles:
                    if role.permissions.administrator or role.permissions.manage_guild or role.permissions.kick_members or role.permissions.ban_members:
                      await after.remove_roles(role)                   

    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member: discord.Member) -> None:
        await self.client.wait_until_ready()

        guild = member.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.ban):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                if guild.me.guild_permissions.ban_members:
                    await guild.ban(entry.user,
                                   reason="R-Dynamic Protection System | Anti ban")
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        await self.client.wait_until_ready()

        guild = member.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.bot_add):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            if member.bot:
                await member.ban(reason="R-Dynamic Protection System | Anti Bot")
                if guild.me.guild_permissions.ban_members:
                    await guild.ban(entry.user,
                                   reason="R-Dynamic Protection System | Anti Bot")

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel) -> None:
        await self.client.wait_until_ready()
        
        
        
        guild = channel.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.channel_create):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                await channel.delete()
                if guild.me.guild_permissions.ban_members:
                    await guild.ban(entry.user,
                                   reason="R-Dynamic Protection System | Anti Channel Create")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel) -> None:
        await self.client.wait_until_ready()

        guild = channel.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.channel_delete):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                await channel.clone()
                await guild.ban(entry.user,
                               reason="R-Dynamic Protection System | Anti Channel Delete")

    @commands.Cog.listener()
    async def on_guild_channel_update(
            self, after: discord.abc.GuildChannel,
            before: discord.abc.GuildChannel) -> None:
        await self.client.wait_until_ready()

        name = before.name
        guild = after.guild
        if not guild:
            return

        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.channel_update):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                await after.edit(name=f"{name}", reason=f"R-Dynamic Protection System | Auto Recovery")
                if guild.me.guild_permissions.ban_members:
                    await guild.ban(entry.user,
                                   reason="R-Dynamic Protection System | Anti Channel Update")

    @commands.Cog.listener()
    async def on_guild_update(self, after: discord.Guild,
                              before: discord.Guild) -> None:
        await self.client.wait_until_ready()

        guild = after
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.guild_update):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                await after.edit(name=f"{before.name}",
                                 reason=f"R-Dynamic Protection System | Auto Recovery")
                if guild.me.guild_permissions.manage_webhooks:
                    await guild.ban(entry.user,
                                  reason="R-Dynamic Protection System | Anti Guild Update")

    @commands.Cog.listener()
    async def on_webhooks_update(self, channel) -> None:
        await self.client.wait_until_ready()

        guild = channel.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.webhook_create):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                await guild.ban(entry.user,
                               reason="R-Dynamic Protection System | Anti Guild Update")
                webhooks = await guild.webhooks()
                for webhook in webhooks:
                    if webhook.id == entry.target.id:
                        if guild.me.guild_permissions.manage_webhooks:
                            await webhook.delete()
                            break

    @commands.Cog.listener()
    async def on_guild_role_create(self, role) -> None:
        await self.client.wait_until_ready()

        guild = role.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.role_create):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                await role.delete()
                if guild.me.guild_permissions.ban_members:
                    await guild.ban(entry.user,
                                   reason="R-Dynamic Protection System | Anti Role Create")

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role) -> None:
        await self.client.wait_until_ready()

        guild = role.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.role_delete):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                rolepos= role.position
                perms= role.permissions
                reas = role.name

                new = await guild.create_role(name = reas , permissions = perms , reason = "R-dynoamic Protection  | Auto Recovery")
                
                await new.edit(position = rolepos)

                if guild.me.guild_permissions.ban_members:
                    await guild.ban(entry.user,
                                   reason="R-Dynamic Protection System | Anti Role Delete")

    @commands.Cog.listener()
    async def on_guild_role_update(self, after: discord.Role,
                                   before: discord.Role) -> None:
        await self.client.wait_until_ready()

        guild = after.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.role_update):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                permissions = before.permissions
                await after.edit(name=f"{before.name}",hoist=f"{before.hoist}",mentionable=f"{before.mentionable}",permissions=permissions,reason="R-Dynamic Protection | Auto Recovery")
                
                if guild.me.guild_permissions.ban_members:
                    await guild.ban(entry.user,
                                   reason="R-Dynamic Protection System | Anti Role Update")

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after) -> None:
        await self.client.wait_until_ready()

        guild = after.guild
        if not guild:
            return
        if not guild.me.guild_permissions.view_audit_log:
            return
        async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.now() - datetime.timedelta(minutes=2),
                action=discord.AuditLogAction.role_update):
            if entry.user.id in IGNORE or entry.user.id == guild.owner.id:
                return
            else:
                permissions = before.permissions
                await after.edit(name=f"{before.name}",
                                 reason=f"R-Dynamic Protection System | Auto Recovery",
                                 permissions=permissions)
                if guild.me.guild_permissions.ban_members:
                    await guild.ban(entry.user,
                                   reason="R-Dynamic Protection System | Anti Role Update")

def setup(client):
	client.add_cog(anti(client))